/* global google */
import React, { Component } from 'react';
import { GoogleApiWrapper, Marker } from 'google-maps-react';
import Api from '../Api'
import MapLocation from '../components/MapLocation'
import UserLocationIcon from '../assets/images/user-location.png';
import YupiStationIcon from '../assets/images/yupi-station.png';
import Card from '../components/Card';
import CardWindow from '../components/CardWindow';

class Looking extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showingInfoWindow: false,
      activeMarker: {},
      selectedPlace: {},
      umbrellas: [],
      showInfoCard: false
    }
  }

  // get all location of umbrellas
  async componentDidMount() {
    try {
      let { data } = await Api.getUmbrellas();
      this.setState({
        umbrellas: data.sombrillas
      });
    } catch (error) {
      console.log(error);
    }
  }

  // show info window component
  onMarkerClick = (props, marker, e) => this.setState({
    selectedPlace: props,
    activeMarker: marker,
    showingInfoWindow: true
  });

  onStartButtonClick = () => this.setState({
    showInfoCard: true,
    showingInfoWindow: false
  })

  onFinishButtonClick = () => this.setState({
    showInfoCard: false
  })

  onClose = () => {
    if (this.state.showingInfoWindow) {
      this.setState({
        showingInfoWindow: false,
        activeMarker: null
      });
    }
  }

  // display stations
  displayUmbrellas = () => {
    return this.state.umbrellas.map((umbrella, index) => {
      return ([
        <Marker 
          key={index} 
          id={index} 
          name={umbrella.id}
          position={{
            lat: umbrella.latitude, 
            lng: umbrella.longitude
          }}
          onClick={this.onMarkerClick}
          icon={{
            url: YupiStationIcon,
            anchor: new google.maps.Point(30,30),
            scaledSize: new google.maps.Size(60,60)
          }}
        />,
        <CardWindow 
          marker={this.state.activeMarker}
          visible={this.state.showingInfoWindow}
          onClose={this.onClose}
        >
          <div className="card">
            <div className="card-body">
              <h5 className="card-title text-center">
                YupiUmbrella #{this.state.selectedPlace.name}
              </h5>
              <button 
                onClick={this.onStartButtonClick}
                className="btn peach-gradient"
              >
                Comenzar
              </button>
            </div>
          </div>
        </CardWindow>
      ])
    })
  }

  render() {
    return (
      <>
        <MapLocation
          centerAroundCurrentLocation
          google={this.props.google}
        >
          <Marker
            icon={{
              url: UserLocationIcon,
              anchor: new google.maps.Point(30,30),
              scaledSize: new google.maps.Size(50,50)
            }}
          />
          { this.displayUmbrellas() }
        </MapLocation>
        <div className="fixed-bottom">
          <Card 
            current={this.state.selectedPlace.name}
            visible={this.state.showInfoCard}
            onClose={this.onFinishButtonClick}
          />
        </div>
      </>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: process.env.REACT_APP_GOOGLE_API_KEY
})(Looking);