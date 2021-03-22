import React from "react";
import { Switch, Route } from "react-router-dom";
import SignIn from "./auth/SignIn";
<<<<<<< HEAD
=======
import SignOut from "./auth/SignOut";
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a
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
<<<<<<< HEAD
            <Route path="/signUp" component={SignUp} />
            <Route path="/signUpDone" component={SignUpDone} />
=======
>>>>>>> 70f61d34bc194eff42376621110ccc530c990b4a

        </Switch>
    </div>
);

export default MainContent;