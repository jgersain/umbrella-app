import axios from 'axios';

// axios configuration 
const client = axios.create({
  baseURL: 'https://angelmartinez04.pythonanywhere.com/api',
  json: true
});

export default {
  async execute(method, resource, data) {
    return client({
      method,
      url: resource,
      data
    }).then(req => req.data)
  },
  getUmbrellas() {
    return this.execute('post', 'graphql', {
      query: `
        query verSombrillas
        {
          sombrillas
          {
            id
            longitude
            latitude
          }  
        }
      `
    })
  }
}