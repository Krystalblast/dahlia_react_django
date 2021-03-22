import React, { Component } from "react";
import { signOutUser } from "../../actions/authActions";
import { Link } from "react-router-dom";

//this component will redirect to user profile after sigin success
class SignInDone extends Component {
    render() {
        return (
        <div>
        <p> Sigin Success!</p>
        <Link to={"/"} className="nav-link" onClick={signOutUser}>
          Sign Out
        </Link>
        </div>
        )
    }
}

export default SignInDone;