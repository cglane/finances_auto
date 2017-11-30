
import React from 'react';

import {DefaultButton} from '../components';
const createReactClass = require('create-react-class');

const AuthenticatePage = createReactClass({
 getInitialState() {
        return {
            value: 'Authenticate'
        };
    },
    render() {
        return (
            <div>
                <h1>Activate </h1>
                <DefaultButton label={'Continue'} onSomeEvent= {this.props.handleChange} path="Upload"> Upload </DefaultButton>
             </div>
            )
        }
})
export default AuthenticatePage