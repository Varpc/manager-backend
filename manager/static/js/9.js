(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{1076:function(t,e,n){"use strict";n.r(e);var o=n(0),r=n.n(o),i=n(870),a=n.n(i),u=n(129),c=n.n(u),l=n(182),f=n.n(l),p=n(187),s=n.n(p),y=n(888);function b(t){return(b="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function t(e){return typeof e}:function t(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(t)}function m(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function h(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}function d(t,e,n){return e&&h(t.prototype,e),n&&h(t,n),t}function v(t,e){return!e||"object"!==b(e)&&"function"!=typeof e?w(t):e}function w(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function g(t){return(g=Object.setPrototypeOf?Object.getPrototypeOf:function t(e){return e.__proto__||Object.getPrototypeOf(e)})(t)}function O(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&E(t,e)}function E(t,e){return(E=Object.setPrototypeOf||function t(e,n){return e.__proto__=n,e})(t,e)}function _(){return(_=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var n=arguments[e];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(t[o]=n[o])}return t}).apply(this,arguments)}var j={variableWidth:!0,centerMode:!0,infinite:!0,dots:!0,adaptiveHeight:!0,autoplay:!0,initialSlide:1,speed:500},S={display:"block",background:"red",opacity:1,margin:"0 20px"},k=function t(e){return r.a.createElement("div",_({id:"prev"},e,{style:S}),r.a.createElement(c.a,{type:"arrow-double-left"}))},P=function t(e){return r.a.createElement("div",_({},e,{style:S}),r.a.createElement(c.a,{type:"arrow-double-right"}))},T,x=function(t){function e(t){var n;return m(this,e),(n=v(this,g(e).call(this,t))).state={images:[]},n}return O(e,t),d(e,[{key:"componentDidMount",value:function t(){var e=this;f.a.get("/api/admin/home/image").then(function(t){var n=t.data.data;1===n.length&&n.push(n[0]),e.setState({images:n})}).catch()}},{key:"componentDidUpdate",value:function t(){var e=document.getElementById("prev");e&&setTimeout(function(){e.click()},50)}},{key:"render",value:function t(){return r.a.createElement("div",{style:{width:"100%",margin:"0",padding:"0"}},r.a.createElement(a.a,_({},j,{nextArrow:r.a.createElement(P,null),prevArrow:r.a.createElement(k,null)}),this.state.images.map(function(t,e){return r.a.createElement("div",{key:e,style:{width:"1000px"}},r.a.createElement(s.a,{width:1e3,height:560,src:t.imgURL,alt:t.name}))})))}}]),e}(r.a.Component),C=n(616),M=n.n(C),R=n(889);function D(t){return(D="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function t(e){return typeof e}:function t(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(t)}function H(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function N(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}function A(t,e,n){return e&&N(t.prototype,e),n&&N(t,n),t}function I(t,e){return!e||"object"!==D(e)&&"function"!=typeof e?J(t):e}function J(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function L(t){return(L=Object.setPrototypeOf?Object.getPrototypeOf:function t(e){return e.__proto__||Object.getPrototypeOf(e)})(t)}function U(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&W(t,e)}function W(t,e){return(W=Object.setPrototypeOf||function t(e,n){return e.__proto__=n,e})(t,e)}var B,q=function(t){function e(t){var n;return H(this,e),(n=I(this,L(e).call(this,t))).state={html:""},n}return U(e,t),A(e,[{key:"componentWillMount",value:function t(){var e=this;f.a.get("/api/admin/home/board").then(function(t){e.setState({html:t.data.html})}).catch(function(t){console.log("board error:",t),e.setState({html:"\u7f51\u7edc\u9519\u8bef\uff0c\u52a0\u8f7d\u5931\u8d25"})})}},{key:"render",value:function t(){return r.a.createElement(M.a,{className:"board-container"},r.a.createElement("div",null,r.a.createElement("div",{className:"title"},"\u516c\u544a"),r.a.createElement("div",{dangerouslySetInnerHTML:{__html:this.state.html}})))}}]),e}(r.a.Component),z=n(890);function F(t){return(F="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function t(e){return typeof e}:function t(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(t)}function G(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function K(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}function Q(t,e,n){return e&&K(t.prototype,e),n&&K(t,n),t}function V(t,e){return!e||"object"!==F(e)&&"function"!=typeof e?X(t):e}function X(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function Y(t){return(Y=Object.setPrototypeOf?Object.getPrototypeOf:function t(e){return e.__proto__||Object.getPrototypeOf(e)})(t)}function Z(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&$(t,e)}function $(t,e){return($=Object.setPrototypeOf||function t(e,n){return e.__proto__=n,e})(t,e)}var tt=function(t){function e(t){var n;return G(this,e),(n=V(this,Y(e).call(this,t))).state={},n}return Z(e,t),Q(e,[{key:"componentDidMount",value:function t(){}},{key:"render",value:function t(){return r.a.createElement("div",null,r.a.createElement(x,null),r.a.createElement(q,null))}}]),e}(o.Component);tt.displayName="Home";var et=e.default=tt},888:function(t,e,n){},889:function(t,e,n){},890:function(t,e,n){}}]);