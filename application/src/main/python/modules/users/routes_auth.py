"""
Authorization controllers for the Users module.

This file is subject to the terms and conditions defined in file 'LICENSE',
which is part of this source code package.
"""

from flask import current_app, jsonify, g

def get_auth_token():
    """Generates an authentication token.

    :returns: JSON string of a token and some other information; status code
    :rtype: (str, int)
    """
    token = g.user.generate_auth_token(
        current_app.config['AUTH_TOKEN_EXPIRATION'], scope=g.auth_scope)
    output = {
        'token': token.decode('ascii'),
        'user_id': g.user.id,
        'username': g.user.username,
        'expiration': current_app.config['AUTH_TOKEN_EXPIRATION']}

    return jsonify(output), 200


def get_auth_token_check():
    """Checks if an authentication token is still valid.

    :returns: JSON string of a `true` value; status code
    :rtype: (str, int)
    """
    return jsonify({'token_check': True}), 200
