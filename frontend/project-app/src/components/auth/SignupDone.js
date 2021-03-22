import React, { Component } from "react";
import { Link } from "react-router-dom";

class SignUpDone extends Component {
    render() {
        return (
            <div className="SignUpDone">
                <h3>
                    Thanks you for your registeration!
                    Please Sign in your account.
                </h3>
                <Link to="/signIn"><button>Sign In</button></Link>
            </div>
        )
    }
}
export default SignUpDone;