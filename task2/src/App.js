// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ProductList from './components/ProductList';
// Import ProductDetail

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={ProductList} />
        {/* Route for ProductDetail */}
      </Switch>
    </Router>
  );
};

export default App;