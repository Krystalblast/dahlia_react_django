import axios from "axios";
import history from "../utils/history";
import { AuthTypes } from "../constants/actionTypes";
import { AuthUrls } from "../constants/urls";
import store from "../store";
import { getUserToken } from "../utils/getUserToken";
import authHeader from "../utils/authHeader";

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
}