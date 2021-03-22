import React, { Component } from "react";
<<<<<<< HEAD
import { signOutUser } from "../../actions/authActions";
=======
import { signoutUser } from "../../actions/authActions";
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
import { Link } from "react-router-dom";

//this component will redirect to user profile after sigin success
class SignInDone extends Component {
    render() {
        return (
        <div>
        <p> Sigin Success!</p>
<<<<<<< HEAD
        <Link to={"/"} className="nav-link" onClick={signOutUser}>
=======
        <Link to={"/"} className="nav-link" onClick={signoutUser}>
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
          Sign Out
        </Link>
        </div>
        )
    }
}

export default SignInDone;