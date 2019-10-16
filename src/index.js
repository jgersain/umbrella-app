import React from 'react';
import ReactDOM from 'react-dom';
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';

import './base.scss';

import App from './components/App/App';

const container = document.getElementById('app');

ReactDOM.render(<App />, container);