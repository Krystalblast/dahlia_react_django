import React, { Component } from "react";

<<<<<<< HEAD
import {reduxForm, Field, propTypes, formValueSelector } from "redux-form";
=======
import {reduxForm, Field, propTypes } from "redux-form";
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
import { Link } from "react-router-dom";
import { required } from "redux-form-validators";

import { signInUser } from "../../actions/authActions";
import { FormControl } from "react-bootstrap";

const renderField = ({ input, label, type, meta: { touched, error } }) => (
    <div>
        <label>{label}</label>
        <div>
            <input className="form-control" {...input} type={type}/>
        </div>
        {touched && ((error && <div className="alert alert-danger p-1"><small>{error}</small></div>))}
    </div>
);
const renderError = (errorMessages) => {
    if (errorMessages) {
        return (
            <div className="alert alert-danger">
                {errorMessages}
            </div>
        )
    }
};

class SignIn extends Component {
  
        static propTypes = {
            ...propTypes
        };
        

    render() {

        const { handleSubmit, error } = this.props;

        return (
            <div className="SignIn">
                <form
                    className="col col-sm-4 cardt mt-5 p-2"
<<<<<<< HEAD
                    onSubmit={handleSubmit}
=======
                    onSubmit={handleSubmit(signInUser)}
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
                >
                    <h2 className="text-md-center">Sign In</h2>
                    <hr/>

<<<<<<< HEAD
                    <fieldset className="form-group">
=======
                    <fieldset className="fomr-group">
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
                        <Field 
                            name="email"
                            label = "Email" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="fomr-group">
                        <Field 
                            name="password"
                            label = "Password" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        { renderError(error) }
                        <button action="submit" className="btn btn-primary">Sign In</button>
                    </fieldset>
                    <br/>
<<<<<<< HEAD
                    <Link to="/signUp"><button>Create New Account</button></Link>
=======
                    <Link to="/signup"><button>Create New Account</button></Link>
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
                    <br/>
                </form>
                                                                
            </div>
        )
    }
}

export default reduxForm({
<<<<<<< HEAD
    form: "signIn",
    onSubmit: signInUser,
=======
    form: "signIn"
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
})(SignIn);
