import { AuthTypes } from "../constants/actionTypes";

export function authReducer(state = {}, action) {
    switch(action.type) {
        case AuthTypes.SIGNIN:
            return { ...state, authenticated: true, token: action.payload};
        case AuthTypes.SIGNOUT:
            return { ...state, authenticated: false, token: null};
        case AuthTypes.USER_PROFILE:
            return { ...state, user: action.payload};
    }
    return state:
}