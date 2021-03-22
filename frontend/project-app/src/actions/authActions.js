import axios from "axios";
<<<<<<< HEAD
=======
import { SubmissionError } from "redux-form";
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
import history from "../utils/history";
import { AuthTypes } from "../constants/actionTypes";
import { AuthUrls } from "../constants/urls";
import store from "../store";
import { getUserToken } from "../utils/getUserToken";
import authHeader from "../utils/authHeader";

<<<<<<< HEAD
import { signInService, signOutService, signUpService } from "../services/authService";
import { formValues } from "redux-form";
import { headers } from "../utils/headers";

export const signUpUser = (formValues) => async dispatch => {
    const res = await axios.post(AuthUrls.SIGN_UP, { ...formValues}, headers);
    dispatch({
        type: AuthTypes,
        payload: res.data
    });
    history.push('/signUpDone');
};

export const signInUser = (formValues) => (dispatch) => {
    return signInService(formValues).then(
        (data) => {
            dispatch({
                type: AuthTypes.SIGN_IN,
                payload: {user: data},
            });
            return Promise.resolve();
        },
        (error) => {
            return Promise.reject();
        }
    );
};

export const signOutUser = () => (dispatch) => {
    signOutService();
    dispatch({
        type: AuthTypes.SIGN_OUT,
    })
=======
export function authSignIn(token) {
    return {
        type: AuthTypes.SIGN_IN,
        payload: token
    };
}

export function signInUser(formValues, dispatch){
    const headers = {
        'Content-Type': 'application/json'
    }
    return axios({
        method: 'POST',
        ulr: AuthUrls.SIGN_IN,
        date: formValues,
        headers: headers,
        responseType: 'json'
    }).then((response) => {
        console.log(response)
        const token = response.data.token;
        dispatch(authSignIn(token));
        localStorage.setItem("token", token);
        history.push("/signInDone");
    }).catch(error => {
        const processedError = processServerError(error.response.data);
        throw new SubmissionError(processedError);
    });
}
/**export function signInUser(formValues, dispatch) {
    const signInUrL = AuthUrls.SIGN_IN;
    const headers = {
        'Content-Type': 'application/json'
    }
    return axios.post(signInUrL, formValues, {headers}).then((response) => {
        const token = response.data.token;
        dispatch(authSignIn(token));

        localStorage.setItem("token", token);

        history.push("/signInDone");
    }).catch(error => {
        console.log(error);
    })
}**/

export function signoutUser(dispatch) {
    localStorage.removeItem("token")
    const signOutUrl = AuthUrls.SIGN_OUT;
    const token = getUserToken(store.getState());
    axios.get(signOutUrl, {
                header: {
                    authorization: 'Token' + token
                }
    }).then((response) => {
        console.log("logout successfully");
    }).catch( error => {
        console.log("logout failed");
    })

    return ({
        type: AuthTypes.SIGN_UP
    });

}

export function signUpUser(formValues, dispatch) {
    const signUpUrl = AuthUrls.SIGN_UP;

    return axios.post(signUpUrl, formValues)
        .then((response) => {
            history.push("/signUpDone")
        })
        .catch((error) => {
            this.errors.push(error)
        });
}

function processServerError(error) {
    return  Object.keys(error).reduce(function(newDict, key) {
        if (key === "non_field_errors") {
            newDict["_error"].push(error[key]);
        } else if (key === "token") {
            // token sent with request is invalid
            newDict["_error"].push("The link is not valid any more.");
        } else {
            newDict[key] = error[key];
        }

        return newDict
    }, {"_error": []});
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
}