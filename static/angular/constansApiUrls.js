angular.module('constansApiUrls', [])

.constant('CONSTANS_URLS', CONSTANS_URLS());

function CONSTANS_URLS(){
    return {
        products_with_purchases: `http://` + window.location.host + `/api/products/with_purchases`,
        product: `http://` + window.location.host + `/api/products/product=`,
        orders_for_product: `http://` + window.location.host + `/api/orders/product=`,
        orders_for_user: `http://` + window.location.host + `/api/orders/user_others=`,
        pending_orders: `http://` + window.location.host + `/api/orders/pending`,
        history_orders: `http://` + window.location.host + `/api/orders/history`,
        active_orders_for_user: `http://` + window.location.host + `/api/orders/user_active=`,
        users: `http://` + window.location.host + `/api/users`,
        user: `http://` + window.location.host + `/api/users/user=`,
        user_purchased_products: `http://` + window.location.host + `/api/users/purchased_products=`,
        user_comments: `http://` + window.location.host + `/api/users/comments_statistic=`,
    };
}

