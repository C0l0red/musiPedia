import React, { Component } from 'react'

export default class CreateSong extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            title: "",
            artist: "",
            featuredArtists: "",
            rating: "",
            album: ""
        }
    }
    
    handleSubmit = event => {
        event.preventDefault();
        console.log(this.state)
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <label>Title</label>
                        <input className="form-control" type="text" id="title" 
                               onChange={event => this.setState({title: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Artist</label>
                        <input className="form-control" type="text" id="artist" 
                               onChange={event => this.setState({artist: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Featured Artists</label>
                        <input className="form-control" type="text" id="featured-artists" 
                               onChange={event => this.setState({featuredArtists: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Album</label>
                        <input className="form-control" type="text" id="album" 
                               onChange={event => this.setState({album: event.target.value})} 
                        />
                    </div>
                    <div className="form-group">
                        <label>Rating</label>
                        <input className="form-control" type="number" id="rating" 
                               onChange={event => this.setState({rating: event.target.value})} 
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Login</button>
                </form>
            </div>
        )
    }
}
