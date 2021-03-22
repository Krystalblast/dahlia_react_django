import React, { Component } from "react";

import {reduxForm, Field, propTypes, formValues } from "redux-form";
import { Link } from "react-router-dom";
import { required } from "redux-form-validators";

import { signUpUser } from "../../actions/authActions";
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

class SignUp extends Component {

    static propTypes = {
        ...propTypes
    };
    render() {
        const { handleSubmit, error } = this.props;

        return (
            <div className="SignUp">
                <form 
                     className="col col-sm-4 cardt mt-5 p-2"
                     onSubmit={handleSubmit}
                >

                    <h2 className="text-md-center">Sign Up</h2>
                    <hr/>                   
        
                    <fieldset className="form-group">
                        <Field 
                            name="username"
                            label = "UserName" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
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
                            name="password1"
                            label = "Password" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="fomr-group">
                        <Field 
                            name="password2"
                            label = "Confirm password" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        <Field 
                            name="first_name"
                            label = "First Name" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        <Field 
                            name="last_name"
                            label = "Last Name" 
                            component = {renderField}
                            type="text"
                            validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        <label>Agency</label>
                        <hr/>
                        <Field
                            name="agency"
                            label="Agency"
                            component="select" 
                        >
                            <option></option>
                            <option value="Au Pair in America">Au Pair in America</option>
                            <option value="Cutural Care Au Pair">Cutural Care Au Pair</option>
                            <option value="AuPairCare">AuPairCare</option>
                            <option value="EurAuPair Intercultural Child Care Programs">EurAuPair Intercultural Child Care Programs</option>
                            <option value="Agent Au Pair">Agent Au Pair</option>
                            <option value="goAUPAIR">goAUPAIR</option>
                            <option value="Au Pair Foundation">Au Pair Foundation</option>
                            <option value="Au Pair 4 Me">Au Pair 4 Me</option>
                            <option value="InterExchange Au Pair USA">InterExchange Au Pair USA</option>
                            <option value="USAupair, Inc.">USAupair, Inc.</option>
                            <option value="Cultural Homestay International Au Pair USA">Cultural Homestay International Au Pair USA</option>
                            <option value="Other">Other</option>
                        </Field>
                        </fieldset>
                        <fieldset className="form-group">
                        { renderError(error) }
                        <button action="submit" className="btn btn-primary">Submit</button>
                                            
                    </fieldset>
                </form>
            </div>
        );
    }
}

const validateForm = values => {
    const errors = {};
    const { password1, password2 } = values;
    if (password1 !== password2) {
        errors.password2 = "Password does not match."
    }
    return errors;
};

export default reduxForm({
    form: "signup",
    validate: validateForm,
    onSubmit: signUpUser,
})(SignUp);