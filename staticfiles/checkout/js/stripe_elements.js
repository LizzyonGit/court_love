/*Adapted from Boutique Ado*/

let stripePublicKey = document.querySelector('#id_stripe_public_key').textContent.slice(1, -1);
let clientSecret = document.querySelector('#id_client_secret').textContent.slice(1, -1);

const stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"IBM Plex Serif", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on card element
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon ps-1" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span class="pe-1">${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';        
    }
});

// Handle form submit
const form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    let submitButton = document.querySelector('#payment-button');
    submitButton.disabled = true;

    let saveInfo = Boolean($('#id-save-info').is(':checked'));
    // From using {% csrf_token %} in the form
    let csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    
    const url = '/checkout/cache_checkout_data/';
    
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.full_name.value),
                            phone: $.trim(form.phone.value),
                            email: $.trim(form.email.value),
                        }
                    },
                    }).then(function(result) {
                        if (result.error) {
                            let errorDiv = document.getElementById('card-errors');
                            let html = `
                                <span class="icon ps-1" role="alert">
                                <i class="fas fa-times"></i>
                                </span>
                                <span class="pe-1">${result.error.message}</span>`;
                            errorDiv.innerHTML = html;
                            card.update({ 'disabled': false});
                            submitButton.disabled = false;
                        } else {
                            if (result.paymentIntent.status === 'succeeded') {
                                //form.submit();
                            }
                        }
                    });
                }).fail(function () {
                    // just reload the page, the error will be in django messages
                    location.reload();
                });       
});