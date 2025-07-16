/*Adapted from Boutique Ado, js instead of jQuery*/

let stripe_public_key = document.querySelector('#id_stripe_public_key').textContent.slice(1, -1);
let client_secret = document.querySelector('#id_client_secret').textContent.slice(1, -1);

const stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"IBM Plex Serif", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {style: style});
card.mount('#card-element');
