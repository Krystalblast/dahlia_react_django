import React, { Component } from 'react';
import './App.css';
import MainContent  from './components/MainContent';

export default class App extends Component {
  render() {
    return (
      <div className="container">
        <MainContent />
      </div>
    );
  }
}

