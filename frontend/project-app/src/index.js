import React from 'react';
import ReactDOM from 'react-dom';
import { Router } from 'react-router-dom';
import { Provider } from 'react-redux';

import store from './store'
import history from './utils/history'
import { authSignIn } from './actions/authActions'
import './index.css';
import App from './App';

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
    <App />
  </Router>
  </Provider>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

