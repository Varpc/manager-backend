(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{1090:function(e,t,n){"use strict";n.r(t);var r=n(0),o=n.n(r),a=n(616),l=n.n(a),i=n(26),c=n(968);function u(e){return(u="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function e(t){return typeof t}:function e(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(e)}function f(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function s(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function p(e,t,n){return t&&s(e.prototype,t),n&&s(e,n),e}function d(e,t){return!t||"object"!==u(t)&&"function"!=typeof t?y(e):t}function y(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function m(e){return(m=Object.setPrototypeOf?Object.getPrototypeOf:function e(t){return t.__proto__||Object.getPrototypeOf(t)})(e)}function b(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&h(e,t)}function h(e,t){return(h=Object.setPrototypeOf||function e(t,n){return t.__proto__=n,t})(e,t)}var g=function(e){function t(e){var n;return f(this,t),(n=d(this,m(t).call(this,e))).state={},n}return b(t,e),p(t,[{key:"render",value:function e(){return o.a.createElement(i.a,null,o.a.createElement("div",{className:"contest-container"},o.a.createElement("div",{className:"page-header"},o.a.createElement("div",{className:"page-title"},"\u6bd4\u8d5b\u7edf\u8ba1")),o.a.createElement(l.a,null,this.props.children)))}}]),t}(o.a.Component),v=t.default=g},615:function(e,t,n){n(615),n(618)},616:function(e,t,n){"use strict";n(615),Object.defineProperty(t,"__esModule",{value:!0});var r,o=a(n(619));function a(e){return e&&e.__esModule?e:{default:e}}t.default=o.default},618:function(e,t,n){},619:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var r,o=d(n(184)),a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},l=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i,c,u=n(0),f=d(u),s,p=d(n(1));function d(e){return e&&e.__esModule?e:{default:e}}function y(e,t){var n={};for(var r in e)t.indexOf(r)>=0||Object.prototype.hasOwnProperty.call(e,r)&&(n[r]=e[r]);return n}function m(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function b(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function h(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}var g=(c=i=function(e){function t(){var e,n,r,o;m(this,t);for(var a=arguments.length,l=Array(a),i=0;i<a;i++)l[i]=arguments[i];return n=r=b(this,(e=t.__proto__||Object.getPrototypeOf(t)).call.apply(e,[this].concat(l))),r.renderChildren=function(){var e=r.props,t=e.error,n=e.empty,o=e.children;return t?f.default.createElement("div",{style:{padding:"80px 0",textAlign:"center"}},f.default.createElement("img",{style:{width:"108px"},src:"https://img.alicdn.com/tfs/TB1KJkbRFXXXXbRXVXXXXXXXXXX-216-218.png",alt:"\u6570\u636e\u52a0\u8f7d\u9519\u8bef"}),f.default.createElement("p",{style:{width:"80%",margin:"30px auto 0",color:"#999",textAlign:"center"}},t)):n?f.default.createElement("div",{style:{padding:"80px 0",textAlign:"center"}},f.default.createElement("img",{style:{width:"97px"},src:"https://img.alicdn.com/tfs/TB1df3oRFXXXXbEXFXXXXXXXXXX-194-220.png",alt:"\u6570\u636e\u4e3a\u7a7a"}),f.default.createElement("p",{style:{width:"80%",margin:"30px auto 0",color:"#999",textAlign:"center"}},n)):o},b(r,o=n)}return h(t,e),l(t,[{key:"render",value:function e(){var t=this.props,n=t.loading,r=t.children,l=t.title,i=t.style,c=t.className,u=t.error,s=t.empty,p=y(t,["loading","children","title","style","className","error","empty"]),d=a({backgroundColor:"#fff",borderRadius:"6px",padding:"20px",marginBottom:"20px"},i);return n?f.default.createElement(o.default,{shape:"fusion-reactor",color:"#66AAFF",style:{width:"100%"}},f.default.createElement("div",{className:"container-block "+c,style:d},r)):f.default.createElement("div",a({className:"container-block "+c,style:d},p),l&&f.default.createElement("h4",{style:{height:"16px",lineHeight:"16px",fontSize:"16px",color:"#333",fontWeight:"bold",margin:0,padding:0,marginBottom:"20px"}},l),this.renderChildren())}}]),t}(u.Component),i.displayName="Container",i.propTypes={loading:p.default.bool,error:p.default.any,empty:p.default.any,style:p.default.object,className:p.default.string,title:p.default.string},i.defaultProps={loading:!1,error:!1,empty:!1,style:{},className:"",title:""},c);t.default=g},968:function(e,t,n){}}]);