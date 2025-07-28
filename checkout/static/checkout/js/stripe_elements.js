/*Adapted from Boutique Ado, js instead of jQuery*/

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

    let saveInfo = Boolean(document.querySelector('#id-save-info').getAttribute('checked'));
    // From using {% csrf_token %} in the form
    let csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    console.log(postData)
    const url = '/checkout/cache_checkout_data/';
    
    // Conversion from jQuery to JS via https://youmightnotneedjquery.com/ and https://md-null0.medium.com/how-to-post-data-to-the-server-using-fetch-method-b961ae18d6fb
    async function postDataFunction(url, postData) {
        try {
            const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
                'save_info': saveInfo,
            })
            });
        
        
            if (response.ok) {
                const result = await response.json(); 

                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: form.querySelector('input[name="full_name"]').value.trim(),
                            phone: form.querySelector('input[name="phone"]').value.trim(),
                            email: form.querySelector('input[name="email"]').value.trim(),
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
                                form.submit();
                            }
                        }
                    })}}
        catch (error) {
            // just reload the page, the error will be in django messages
            location.reload();
        }
    };
    
    postDataFunction(url, postData)          
});