from application import app, db, api, cache
from flask import render_template, request, Response, json, jsonify, flash, redirect, url_for, session
import datetime
import time
from application.models import Products
from application.utils import encoder
from flask_restplus import Resource, abort
from flask_jwt_simple import jwt_required, create_jwt, get_jwt_identity



##### API ENDPOINTS #####
    
    
###### PRODUCTS #####

@api.route('/products', '/products/' )
class ProductsGetAll(Resource):
    
    # GET ALL
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self):
        return jsonify(Products.objects.all())
    
    
@api.route('/products/<txt>')
class ProductByWord(Resource):
    
    # GET PRODUCTS SEARCH BY 1 MATCH IN NAME
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self, txt: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*', 
                        '$options':'i'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
        
        return json.loads(resp_string), 200
    
    
@api.route('/products/<txt>+<txt_>')
class ProductBy2Words(Resource):
    
    # GET PRODUCTS SEARCH BY 2 MATCHES IN NAME
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self, txt: str, txt_: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*' + '.*' + txt_ + '.*',
                        '$options': 'i'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
        
        return json.loads(resp_string), 200
    
    

@api.route('/products/<txt>+<txt_>+<txt_1>')
class ProductBy3Words(Resource):
    
    # GET PRODUCTS SEARCH BY 3 MATCHES IN NAME
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self, txt: str, txt_: str, txt_1: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*' + '.*' + txt_ + '.*' + '.*' + txt_1 + '.*', 
                        '$options':'i'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
        
        return json.loads(resp_string), 200
    
    
@api.route('/products/<txt>+<txt_>+<txt_1>+<txt_2>')
class ProductBy4Words(Resource):
    
    # GET PRODUCTS SEARCH BY 4 MATCHES IN NAME
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self, txt: str, txt_: str, txt_1: str, txt_2: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*' + '.*' + txt_ + '.*' + '.*' + txt_1 + '.*' + '.*' + txt_2 + '.*', 
                        '$options':'i'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
        
        return json.loads(resp_string), 200
    
    
@api.route('/products/<txt>+<txt_>+<txt_1>+<txt_2>+<txt_3>')
class ProductBy5Words(Resource):
    
    # GET PRODUCTS SEARCH BY 5 MATCHES IN NAME
    # @jwt_required
    @cache.cached(timeout=50)
    def get(self, txt: str, txt_: str, txt_1: str, txt_2: str, txt_3: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*' + '.*' + txt_ + '.*' + '.*' + txt_1 + '.*' + '.*' + txt_2 + '.*' + '.*' + txt_3 + '.*', 
                        '$options':'i'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
            
        
        return json.loads(resp_string), 200
    



# @api.route('/products/<int:idx>')
# class ProductById(Resource):
    
#     # GET ONE BY INDEX
#     # @jwt_required
#     @cache.cached(timeout=50)
#     def get(self, idx: int):
#         return jsonify(Products.objects(id=idx))
  
  
# @api.route('/products/slug/<slug>')
# class ProductBySlug(Resource):
    
#     # GET ONE
#     # @jwt_required
#     @cache.cached(timeout=50)
#     def get(self, slug: str):
    
#         resp = Products.objects.aggregate(*[
#             {
#                 '$match': {
#                     'slug': {
#                         '$regex': '.*' + slug + '.*', 
#                         '$options':'i'
#                     }
#                 }
#             }
#         ])
        
#         resp_string = encoder.encode(list(resp))
        
#         return json.loads(resp_string), 200

        
    


