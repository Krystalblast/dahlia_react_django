import React from "react";
import { Switch, Route } from "react-router-dom";
import SignIn from "./auth/SignIn";
import SignOut from "./auth/SignOut";
import SignUp from "./auth/SignUp";
import SignUpDone from "./auth/SignUpDone";
import SignInDone from "./auth/SignInDone";
//import NoMatch from "./Nomatch";

const MainContent = () => (
    <div>
        <Switch>
            <Route exact path="/" component={SignIn}/>
            <Route path="/signIn" component={SignIn}/>
            <Route path="/signInDone" component={SignInDone}/>
            <Route path="/signUp" component={SignUp} />
            <Route path="/signUpDone" component={SignUpDone} />
        </Switch>
    </div>
);

export default MainContent;