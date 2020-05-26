angular.module('constansApiUrls', [])

.constant('CONSTANS_URLS', CONSTANS_URLS());

function CONSTANS_URLS(){
    return {
        products_with_purchases: `http://` + window.location.host + `/api/products/with_purchases`,
        product: `http://` + window.location.host + `/api/products/product=`,
        orders_for_product: `http://` + window.location.host + `/api/orders/product=`,
    };
}

