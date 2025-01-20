from src.Stores import Stores

html_content = """
<div class="table-content">

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">1</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://store.goo.ne.jp/cdn/shop/files/favicon_96x96.png"
                alt="Goo Ne store logo">

            <div class="shop-name"><a href="https://store.goo.ne.jp" target="_blank">Goo Ne</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            161.51M
        </div>
        <div class="column-item column-item6">
            12.92M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">2</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://store.ign.com/cdn/shop/files/favicon_a3cc2658-8654-4535-8029-e9d7aaf7b7a9.png"
                alt="Ign store logo">

            <div class="shop-name"><a href="https://store.ign.com" target="_blank">Ign</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Toys &amp; game
        </div>
        <div class="column-item column-item5">
            90.66M
        </div>
        <div class="column-item column-item6">
            3.63M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/ignstore/" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://instagram.com/ignstore" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/IGNStore" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">3</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://cdn.shopify.com/s/files/1/0125/3336/6848/files/Store-logo_7dc0e2e0-14b3-468e-8229-b4cf8dca8faa_400x63.png?v=1613763490"
                alt="Breitbart store logo">

            <div class="shop-name"><a href="https://store.breitbart.com" target="_blank">Breitbart</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            44.98M
        </div>
        <div class="column-item column-item6">
            3.60M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/Breitbart" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/wearebreitbart/" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/BreitbartNews" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/channel/UCmgnsaQIK1IR808Ebde-ssA"
                target="_blank" aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">4</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://store.asoview.com/cdn/shop/files/favicon.png" alt="Asoview store logo">

            <div class="shop-name"><a href="https://store.asoview.com" target="_blank">Asoview</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            2021
        </div>
        <div class="column-item column-item5">
            5.50M
        </div>
        <div class="column-item column-item6">
            1.96M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><a
                href="https://www.instagram.com/asoviewgift/" target="_blank" aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">5</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://nothing.tech/cdn/shop/files/favicon_32x32.png" alt="Nothing store logo">

            <div class="shop-name"><a href="https://nothing.tech" target="_blank">Nothing</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Consumer Electronics
        </div>
        <div class="column-item column-item5">
            3.62M
        </div>
        <div class="column-item column-item6">
            1.56M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><a
                href="https://www.instagram.com/nothing/?hl=en" target="_blank" aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/nothing" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://youtube.com/c/NothingTechnology" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">6</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://traya.health/cdn/shop/files/favicon-32x32_256x256_1a53794d-d934-47fc-824d-b0e3862279e9.webp"
                alt="Traya store logo">

            <div class="shop-name"><a href="https://traya.health" target="_blank">Traya</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Beauty &amp; Health
        </div>
        <div class="column-item column-item5">
            370.71K
        </div>
        <div class="column-item column-item6">
            1.38M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/traya.health/" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/traya.health/" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/TrayaHealth?t=I0O9cO7MJi-iIHiVSqI9qg&amp;s=09"
                target="_blank" aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/@TrayaHealth" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">7</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://rtshop.radiotimes.com/cdn/shop/files/favicon_12454066-743b-4fb1-aa23-659bbb311396_32x32.jpg"
                alt="Radiotimes store logo">

            <div class="shop-name"><a href="https://rtshop.radiotimes.com" target="_blank">Radiotimes</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            15.88M
        </div>
        <div class="column-item column-item6">
            1.27M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">8</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://suscripciones.groupbrands.net/cdn/shop/files/favicon-forbes_32x32.jpg"
                alt="Groupbrands store logo">

            <div class="shop-name"><a href="https://suscripciones.groupbrands.net" target="_blank">Groupbrands</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            474
        </div>
        <div class="column-item column-item6">
            1.17M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/ForbesMexico" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/forbesmexico/?hl=es" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/Forbes_Mexico" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/user/forbesmexico" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><a href="https://www.pinterest.com/forbesmexico/" target="_blank"
                aria-label="pinterest"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest.png" alt="pinterest"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">9</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://store.covenanteyes.com/cdn/shop/files/favicon_32x32.png"
                alt="Covenanteyes store logo">

            <div class="shop-name"><a href="https://store.covenanteyes.com" target="_blank">Covenanteyes</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            1.86M
        </div>
        <div class="column-item column-item6">
            1.17M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/CovenantEyes" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><a
                href="https://twitter.com/covenanteyes" target="_blank" aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/covenanteyes" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">10</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://boutique.liberation.fr/cdn/shop/files/LOGO-BOUTIQUE-LIBE_32x32.png"
                alt="Liberation store logo">

            <div class="shop-name"><a href="https://boutique.liberation.fr" target="_blank">Liberation</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Toys &amp; game
        </div>
        <div class="column-item column-item5">
            14.44M
        </div>
        <div class="column-item column-item6">
            1.16M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">11</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <div class="shop-letter">G</div>

            <div class="shop-name"><a href="https://www.gymshark.com" target="_blank">Gymshark</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            22.80M
        </div>
        <div class="column-item column-item6">
            1.14M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">12</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <div class="shop-letter">H</div>

            <div class="shop-name"><a href="https://store.hammer.ucla.edu" target="_blank">Hammer Ucla</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            13.66M
        </div>
        <div class="column-item column-item6">
            1.09M
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/HammerMuseum" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://instagram.com/hammer_museum" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/hammer_museum" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/user/hammermuseum" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">13</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://store.corrieredellosport.it/cdn/shop/files/corsport_32x32.png"
                alt="Corrieredellosport store logo">

            <div class="shop-name"><a href="https://store.corrieredellosport.it" target="_blank">Corrieredellosport</a>
            </div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            13.52M
        </div>
        <div class="column-item column-item6">
            1.08M
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">14</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://cdn.shopify.com/s/files/1/0070/5698/2143/files/favicon_32x32.jpg"
                alt="Wwe store logo">

            <div class="shop-name"><a href="https://shop.wwe.com" target="_blank">Wwe</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            12.17M
        </div>
        <div class="column-item column-item6">
            973.36K
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">15</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://www.vqfit.com/cdn/shop/files/babycon_180x180.png" alt="Vqfit store logo">

            <div class="shop-name"><a href="https://www.vqfit.com" target="_blank">Vqfit</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            565.57K
        </div>
        <div class="column-item column-item6">
            952.00K
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/vqfitofficial" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/vqfit" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><a
                href="https://www.youtube.com/channel/UCppSW2d__oJ87d5FDxyEEVQ" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">16</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://cdn.shopify.com/s/files/1/1367/5207/files/Favicon-White-Circle_32x32.png"
                alt="Ibsz store logo">

            <div class="shop-name"><a href="https://ibsz.xyz" target="_blank">Ibsz</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            22.80M
        </div>
        <div class="column-item column-item6">
            912.00K
        </div>
        <div class="column-item column-item7">
            <img src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook_gray.png"
                alt="facebook_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram_gray.png"
                alt="instagram_gray"
                style="width: 21px;margin-right: 7px;margin-left: 3px;position: relative;top: -1px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter_gray.png"
                alt="twitter_gray" style="width: 24px;margin-right: 4px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">17</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://spicestore.stanford.edu/cdn/shop/files/Stanford_SPICE_500x500_f1dc0797-04aa-4e14-91d3-1979bccdc8b1_32x32.png"
                alt="Stanford store logo">

            <div class="shop-name"><a href="https://spicestore.stanford.edu" target="_blank">Stanford</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Office &amp; School Supplies
        </div>
        <div class="column-item column-item5">
            21.03M
        </div>
        <div class="column-item column-item6">
            841.37K
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/stanfordspice" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/stanford.spice" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/StanfordSPICE" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/StanfordSPICE" target="_blank"
                aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">18</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://uk.gear.blizzard.com/cdn/shop/files/Blizz_Gear_Logo_RGB_DarkBkgd_32x32.png"
                alt="Gear Blizzard store logo">

            <div class="shop-name"><a href="https://uk.gear.blizzard.com" target="_blank">Gear Blizzard</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Can Cooler
        </div>
        <div class="column-item column-item5">
            19.51M
        </div>
        <div class="column-item column-item6">
            780.36K
        </div>
        <div class="column-item column-item7">
            <a href="https://facebook.com/Blizzard" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://instagram.com/blizzard" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/blizzard_ent" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">19</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img"
                src="https://cdn.shopify.com/s/files/1/0006/4189/2410/files/snopes-icon-square-full-color-yellow.png"
                alt="Snopes store logo">

            <div class="shop-name"><a href="https://shop.snopes.com" target="_blank">Snopes</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Clothing, Shoes &amp; Jewelry
        </div>
        <div class="column-item column-item5">
            9.71M
        </div>
        <div class="column-item column-item6">
            776.84K
        </div>
        <div class="column-item column-item7">
            <a href="https://facebook.com/snopes" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://instagram.com/snopesdotcom" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://twitter.com/snopes" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube_gray.png"
                alt="youtube_gray" style="width: 24px;margin-right: 2px;"><a href="https://pinterest.com/snopesdotcom"
                target="_blank" aria-label="pinterest"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest.png" alt="pinterest"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

    <div class="row-item">
        <div class="column-item column-item1">
            <div class="sort">20</div>
        </div>
        <div class="column-item column-item2 column-shop">

            <img class="shop-img" src="https://au-en.ring.com/cdn/shop/t/2/assets/favicon.ico" alt="Ring store logo">

            <div class="shop-name"><a href="https://nz-en.ring.com" target="_blank">Ring</a></div>
        </div>
        <div class="column-item column-item3">
            Shopify
        </div>
        <div class="column-item column-item4">
            Multipacks
        </div>
        <div class="column-item column-item5">
            19.12M
        </div>
        <div class="column-item column-item6">
            764.67K
        </div>
        <div class="column-item column-item7">
            <a href="https://www.facebook.com/ring" target="_blank" aria-label="facebook"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/facebook.png" alt="facebook"
                    style="width: 24px;"></a><a href="https://www.instagram.com/ring" target="_blank"
                aria-label="instagram"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/instagram.png" alt="instagram"
                    style="width: 24px;"></a><a href="https://www.twitter.com/ring" target="_blank"
                aria-label="twitter"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/twitter.png" alt="twitter"
                    style="width: 24px;"></a><a href="https://www.youtube.com/channel/UC22Bt8xIq_IWYMTXAJ4Idow"
                target="_blank" aria-label="youtube"><img
                    src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/youtube.png" alt="youtube"
                    style="width: 24px;"></a><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/pinterest_gray.png"
                alt="pinterest_gray"
                style="width: 21px;margin-right: 2px;margin-left: 4px;position: relative;top: -2px;"><img
                src="https://static-oss-cdn.oss-us-west-1.aliyuncs.com/sc/static/img/snapchat_gray.png"
                alt="snapchat_gray" style="width: 24px;margin-right: 2px;">
        </div>
    </div>

</div>"""

print(Stores.save('shopify', 'username@example.com', html_content))