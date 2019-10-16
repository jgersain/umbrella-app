import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Layout from '../Layout';
import Home from '../../pages/Home';

const App = () => (
  <BrowserRouter>
    <Layout>
      <Switch>
        <Route exact path="/" component={ Home } />
      </Switch>
    </Layout>
  </BrowserRouter>
);

export default App;