import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import reducer from './reducers'
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';

import './base.scss';

import App from './components/App';

const initialState = {
  "users": [
    {
      "id": 1,
      "name": "Hugo"
    },
    {
      "id": 2,
      "name": "Paco"
    },
    {
      "id": 3,
      "name": "Luis"
    }
  ]
}

const store = createStore(reducer, initialState);

const container = document.getElementById('app');

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>, 
  container
);
