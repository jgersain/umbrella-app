import React from 'react';
import { MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavbarToggler, MDBCollapse, MDBNavItem, MDBNavLink, MDBContainer } from 'mdbreact';
import { withRouter } from "react-router-dom";

import Logo from '../assets/images/yupi-station.png';
import { AUTH_TOKEN } from '../constants';


class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      collapse: false,
      isWideEnough: false,
    };
    this.onClick = this.onClick.bind(this);
  }

  onClick() {
    this.setState({
      collapse: !this.state.collapse,
    });
  }

  render() {
    const authToken = localStorage.getItem(AUTH_TOKEN);

    return (
      <header>
        <MDBNavbar color="purple-gradient" fixed="top" dark expand="md" scrolling>
          <MDBContainer>
            <MDBNavbarBrand href="/">
              <img src={Logo} width={40} height={40} alt="logo"/>
              <strong>
                <span className="font-weight-bold text-warning yupi yupi-tiny">
                  YupiApp
                </span>
              </strong>
            </MDBNavbarBrand>
            {!this.state.isWideEnough && <MDBNavbarToggler onClick={this.onClick}/>}
            <MDBCollapse isOpen={this.state.collapse} navbar>
              <MDBNavbarNav right>
                {authToken ? (
                  <li className="nav-item">
                    <span 
                      className="nav-link font-weight-bold text-default"
                      onClick={() => {
                        localStorage.removeItem(AUTH_TOKEN)
                        this.props.history.push(`/`)
                      }}
                    >
                      Registrate
                    </span>
                  </li>
                ) : (
                  <MDBNavItem>
                    <MDBNavLink to="/login" className="font-weight-bold text-warning">Iniciar Sesión</MDBNavLink>
                  </MDBNavItem>
                )}
              </MDBNavbarNav>
            </MDBCollapse>
          </MDBContainer>
        </MDBNavbar>
      </header>
    );
  }
}

export default withRouter(Header);