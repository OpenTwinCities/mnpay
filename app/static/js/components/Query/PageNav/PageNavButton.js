import React from "react";

export default class PageNavButton extends React.Component {

  handleClick(e){
    this.props.handleClick(this.props.pageValue)
  }

  render() {
    var className="";
    if (this.props.active){
      className="active"
    }
    return (
      <li className={className} onClick={this.handleClick.bind(this)}>
        <a>{this.props.displayText}</a>
      </li>
    );
  }
}
