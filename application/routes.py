from application import app, db, api
from flask import render_template, request, Response, json, jsonify, flash, redirect, url_for, session
import datetime
import time
from application.models import Products
from application.utils import encoder
from flask_restplus import Resource, abort
from flask_jwt_simple import jwt_required, create_jwt, get_jwt_identity



##### API ENDPOINTS #####
    
    
###### PRODUCTS #####

@api.route('/products')
class ProductsGetAll(Resource):
    
    # GET ALL
    # @jwt_required
    def get(self):
        return jsonify(Products.objects.all())
    
    
        

@api.route('/products/<int:idx>')
class ProductById(Resource):
    
    # GET ONE
    # @jwt_required
    def get(self, idx: int):
        return jsonify(Products.objects(id=idx))
    
@api.route('/products/<txt>')
class ProductByName(Resource):
    
    # GET ONE
    # @jwt_required
    def get(self, txt: str):
    
        resp = Products.objects.aggregate(*[
            {
                '$match': {
                    'name': {
                        '$regex': '.*' + txt + '.*'
                    }
                }
            }
        ])
        
        resp_string = encoder.encode(list(resp))
        
        return json.loads(resp_string), 200

        
    


