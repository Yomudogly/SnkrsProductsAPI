import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash


class Products(db.Document):

    id = db.StringField( max_lenght=50 )
    company_id = db.StringField( max_lenght=50 )
    product_id = db.StringField( max_lenght=50 )
    discount_id = db.StringField( max_lenght=50 )
    name = db.StringField( max_lenght=50 )
    position = db.StringField( max_lenght=50 )
    brand_id = db.StringField( max_lenght=50 )
    brand_name = db.StringField( max_lenght=50 )
    model_cat_id = db.StringField( max_lenght=50 )
    model_cat = db.StringField( max_lenght=50 )
    brief_description = db.StringField( max_lenght=50 )
    description = db.StringField( max_lenght=50 )
    visit = db.StringField( max_lenght=50 )
    sale = db.StringField( max_lenght=50 )
    expires_at = db.StringField( max_lenght=50 )
    keywords = db.StringField( max_lenght=50 )
    url = db.StringField( max_lenght=50 )
    shape1 = db.StringField( max_lenght=50 )
    shape2 = db.StringField( max_lenght=50 )
    shape3 = db.StringField( max_lenght=50 )
    shape4 = db.StringField( max_lenght=50 )
    shape5 = db.StringField( max_lenght=50 )
    shape6 = db.StringField( max_lenght=50 )
    shape7 = db.StringField( max_lenght=50 )
    shape8 = db.StringField( max_lenght=50 )
    img_box = db.StringField( max_lenght=50 )
    img_lateral = db.StringField( max_lenght=50 )
    img_medial = db.StringField( max_lenght=50 )
    img_heel = db.StringField( max_lenght=50 )
    img_top = db.StringField( max_lenght=50 )
    img_soles = db.StringField( max_lenght=50 )
    img_tag = db.StringField( max_lenght=50 )
    sku = db.StringField( max_lenght=50 )
    stock = db.StringField( max_lenght=50 )
    stock_min = db.StringField( max_lenght=50 )
    is_active = db.StringField( max_lenght=50 )
    stars = db.StringField( max_lenght=50 )
    price = db.StringField( max_lenght=50 )
    regular_price = db.StringField( max_lenght=50 )
    weight = db.StringField( max_lenght=50 )
    length = db.StringField( max_lenght=50 )
    width = db.StringField( max_lenght=50 )
    height = db.StringField( max_lenght=50 )
    type_id = db.StringField( max_lenght=50 )
    seo_title = db.StringField( max_lenght=50 )
    seo_description = db.StringField( max_lenght=50 )
    seo_keywords = db.StringField( max_lenght=50 )
    shortcut = db.StringField( max_lenght=50 )
    lowest_ask = db.StringField( max_lenght=50 )
    highest_offer = db.StringField( max_lenght=50 )
    most_recent = db.StringField( max_lenght=50 )
    user_id = db.StringField( max_lenght=50 )
    user_name   = db.StringField( max_lenght=50 )
    created_at = db.StringField( max_lenght=50 )
    updated_at = db.StringField( max_lenght=50 )
    slug = db.StringField( max_lenght=50 )
    image = db.StringField( max_lenght=50 )
    image0 = db.StringField( max_lenght=50 )
    image1 = db.StringField( max_lenght=50 )
    image2 = db.StringField( max_lenght=50 )
    image3 = db.StringField( max_lenght=50 )
    image4 = db.StringField( max_lenght=50 )
    image5 = db.StringField( max_lenght=50 )