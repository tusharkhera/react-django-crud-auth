import React, { Component} from 'react';

class Quote extends Component {

  state = {
    quotes: []
  }

  loadQuotes = () => {
    fetch('http://127.0.0.1:8000/quotes/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${this.props.token}`
      },
      body: JSON.stringify(this.state.credentials)
    })
    .then( data => data.json())
    .then(
      data => {
        this.setState({quotes: data})
      }
    )
    .catch( error => console.error(error))
  }

  render() {
    return (
      <div>
        <h1>Quotes</h1>
        { this.state.quotes.map( quote => {
          return <h3 key={quote.id}>{quote.quote}</h3>
        })}
        <button onClick={this.loadQuotes}>Load Quotes</button>
      </div>
    );
  }
}

export default Quote;
