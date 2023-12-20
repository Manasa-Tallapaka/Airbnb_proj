# main/main.py

from flask import Flask, request, jsonify
from utils.data_handler import read_data, write_data

app = Flask(__name__)

# Read initial data from JSON file
listings = read_data("data/airbnb.json")


# GET Endpoints
@app.route('/listings', methods=['GET'])
def get_all_listings():
    return jsonify(listings), 200


@app.route('/listings/<int:listing_id>', methods=['GET'])
def get_listing_by_id(listing_id):
    listing = next((l for l in listings if l['id'] == listing_id), None)
    if listing:
        return jsonify(listing), 200
    else:
        return jsonify({"error": "Listing not found"}), 404


@app.route('/listings', methods=['GET'])
def get_listings_by_query():
    # Example: /listings?price_gt=100&neighborhood=Downtown
    filters = {key: request.args.get(key) for key in request.args}
    filtered_listings = [l for l in listings if all(l.get(k) == v for k, v in filters.items())]
    return jsonify(filtered_listings), 200


# POST Endpoint
@app.route('/listings', methods=['POST'])
def create_listing():
    new_listing = request.json
    new_listing['id'] = max(listing['id'] for listing in listings) + 1
    listings.append(new_listing)
    write_data("data/airbnb.json", listings)
    return jsonify({"message": "Listing created successfully"}), 201


# PATCH Endpoint
@app.route('/listings/<int:listing_id>', methods=['PATCH'])
def update_listing(listing_id):
    listing = next((l for l in listings if l['id'] == listing_id), None)
    if listing:
        update_data = request.json
        listing.update(update_data)
        write_data("data/airbnb.json", listings)
        return jsonify({"message": "Listing updated successfully"}), 200
    else:
        return jsonify({"error": "Listing not found"}), 404


# DELETE Endpoint
@app.route('/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    global listings
    listings = [l for l in listings if l['id'] != listing_id]
    write_data("data/airbnb.json", listings)
    return jsonify({"message": "Listing deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
