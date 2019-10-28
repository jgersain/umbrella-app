import React from 'react';
import { Link } from 'react-router-dom';
import { MDBView, MDBMask } from 'mdbreact';

import backgroundImage from '../assets/images/background.jpg';
import './styles/Home.scss'

const Home = () => (
  <MDBView src={ backgroundImage }>
    <MDBMask overlay="purple-light" className="flex-center flex-column text-white text-center">
      <h1 className="font-weight-bold text-warning yupi yupi-big">Yupi App</h1>
      <h4 className="m-4">Yupi es un sevicio simple, accesible y útil que permite a los usuarios rentar y devolver paraguas.</h4>
      <Link className="btn peach-gradient font-weight-bold" to='sign_up/'>Registrate</Link>
    </MDBMask>
  </MDBView>
);

export default Home;
