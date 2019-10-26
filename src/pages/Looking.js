/* global google */
import React, { Component } from 'react';
import { GoogleApiWrapper, Marker, InfoWindow } from 'google-maps-react';

import MapLocation from '../components/MapLocation'
import UserLocationIcon from '../assets/images/user-location.png';
import YupiStationIcon from '../assets/images/yupi-station.png';

class Looking extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showingInfoWindow: false,
      activeMarker: {},
      selectedPlace: {},
      stations: [
        {
          name: 'YupiStation Torre del Caballito',
          latitude: 19.436595,
          longitude: -99.148838
        },
        {
          name: 'YupiStation Plaza de la República',
          latitude: 19.436468,
          longitude: -99.154063
        },
        {
          name: 'YupiStation Le Meridién',
          latitude: 19.433985,
          longitude: -99.154439
        },
        {
          name: 'YupiStation Museo Nacional de San Carlos',
          latitude: 19.438284,
          longitude: -99.152067
        },
        {
          name: 'YupiStation Fiesta America',
          latitude: 19.432720,
          longitude: -99.154986
        },
        {
          name: 'YupiStation Test',
          latitude: 19.618602,
          longitude: -99.066066
        }
      ]
    }
  }

  // show info window component
  onMarkerClick = (props, marker, e) => this.setState({
    selectedPlace: props,
    activeMarker: marker,
    showingInfoWindow: true
  });


  onClose = () => {
    if (this.state.showingInfoWindow) {
      this.setState({
        showingInfoWindow: false,
        activeMarker: null
      });
    }
  }

  // display stations
  displayStations = () => {
    return this.state.stations.map((station, index) => {
      return ([
        <Marker 
          key={index} 
          id={index} 
          name={station.name}
          position={{
            lat: station.latitude, 
            lng: station.longitude
          }}
          onClick={this.onMarkerClick}
          icon={{
            url: YupiStationIcon,
            anchor: new google.maps.Point(30,30),
            scaledSize: new google.maps.Size(60,60)
          }}
        />,
        <InfoWindow 
          marker={this.state.activeMarker}
          visible={this.state.showingInfoWindow}
          onClose={this.onClose}
        >
          <div>
            <h4>{this.state.selectedPlace.name}</h4>
          </div>
        </InfoWindow>
      ])
    })
  }

  render() {
    return (
      <MapLocation
        centerAroundCurrentLocation
        google={this.props.google}
      >
        <Marker 
          onClick={this.onMarkerClick} 
          name={'Current location'}
          icon={{
            url: UserLocationIcon,
            anchor: new google.maps.Point(30,30),
            scaledSize: new google.maps.Size(50,50)
          }}
        />
        <InfoWindow
          marker={this.state.activeMarker}
          visible={this.state.showingInfoWindow}
          onClose={this.onClose}
        >
          <div>
            <h4>{this.state.selectedPlace.name}</h4>
          </div>
        </InfoWindow>
        { this.displayStations() }
      </MapLocation>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: process.env.REACT_APP_GOOGLE_API_KEY
})(Looking);