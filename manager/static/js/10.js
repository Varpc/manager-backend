(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{1085:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),o=n(699),i=n.n(o),l=n(75),u=n.n(l),s=n(915),c=n.n(s),f=n(628),p=n.n(f),d=n(84),h=n.n(d),y=n(1071),m=n(182),b=n.n(m),v=n(932);function g(e){return(g="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function e(t){return typeof t}:function e(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(e)}function S(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function E(e,t){for(var n=0;n<t.length;n++){var a=t[n];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}function w(e,t,n){return t&&E(e.prototype,t),n&&E(e,n),e}function I(e,t){return!t||"object"!==g(t)&&"function"!=typeof t?P(e):t}function O(e){return(O=Object.setPrototypeOf?Object.getPrototypeOf:function e(t){return t.__proto__||Object.getPrototypeOf(t)})(e)}function x(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&C(e,t)}function C(e,t){return(C=Object.setPrototypeOf||function e(t,n){return t.__proto__=n,t})(e,t)}function P(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}var j=h.a.toast,N=function(e){function t(e){var n;return S(this,t),(n=I(this,O(t).call(this,e))).handlePagination=function(e){n.setState({current:e})},n.handleSort=function(e,t){var a=n.state.dataSource.sort(function(n,a){var r=n[e]-a[e];return"asc"===t?r>0?1:-1:r>0?-1:1});n.setState({dataSource:a})},n.renderState=function(e){return 0===e?r.a.createElement("div",{className:"state"},r.a.createElement("span",{className:"circle-blue"}),r.a.createElement("span",{className:"state-text-blue"},"\u5ba1\u6838")):1===e?r.a.createElement("div",{className:"state"},r.a.createElement("span",{className:"circle-green"}),r.a.createElement("span",{className:"state-text-green"},"\u73b0\u5f79")):2===e?r.a.createElement("div",{className:"state"},r.a.createElement("span",{className:"circle-blue"}),r.a.createElement("span",{className:"state-text-blue"},"\u9000\u5f79")):3===e?r.a.createElement("div",{className:"state"},r.a.createElement("span",{className:"circle-red"}),r.a.createElement("span",{className:"state-text-red"},"\u9664\u540d")):void 0},n.renderName=function(e){return r.a.createElement(y.a,{to:"/myhome/".concat(e.user_id)},e.name)},n.setDataSource=function(e){var t=[];n.state.data.map(function(n){return(""===e||n.user.name.includes(e)||n.user.banji.includes(e))&&t.push(n),n.id}),n.setState({dataSource:t})},n.onSerchChange=function(e){n.setDataSource(e)},n.onSearch=function(e){n.setDataSource(e.key)},n.setDataSourceNow=function(){var e=[];n.state.data.map(function(t){return 1===t.user.status&&e.push(t),t.id}),n.setState({dataSource:e})},n.setDataSourceAll=function(){n.setDataSource("")},n.state={current:1,pageSize:30,isLoading:!0,data:[],dataSource:[]},n.handlePageSizeChange=n.handlePageSizeChange.bind(P(P(n))),n}return x(t,e),w(t,[{key:"componentDidMount",value:function e(){var t=this;b.a.get("/api/problems").then(function(e){t.state.data=e.data.data,t.setState({data:t.state.data.concat(),dataSource:t.state.data.concat(),isLoading:!1})}).catch(function(e){j.error("\u7f51\u7edc\u9519\u8bef\uff0c\u8bf7\u7a0d\u540e\u91cd\u8bd5"),console.log(e),t.setState({isLoading:!1})})}},{key:"handlePageSizeChange",value:function e(t){this.setState({pageSize:t})}},{key:"tableRender",value:function e(){for(var t=this.state.dataSource,n=(this.state.current-1)*this.state.pageSize,a=this.state.current*this.state.pageSize,o=[],i=n;i<a&&i<t.length;i+=1)o.push(t[i]);return r.a.createElement(p.a,{dataSource:o,onSort:this.handleSort,isLoading:this.state.isLoading,hasBorder:!1,className:"custom-table"},r.a.createElement(p.a.Column,{title:"\u5e8f\u5217\u53f7",dataIndex:"user.user_id"}),r.a.createElement(p.a.Column,{title:"\u59d3\u540d",dataIndex:"user",cell:this.renderName}),r.a.createElement(p.a.Column,{title:"\u73ed\u7ea7",dataIndex:"user.banji"}),r.a.createElement(p.a.Column,{title:"\u603b\u8ba1",dataIndex:"sum",sortable:!0}),r.a.createElement(p.a.Column,{title:"\u84dd\u4e66",dataIndex:"blue_book"}),r.a.createElement(p.a.Column,{title:"\u7d2b\u4e66",dataIndex:"purple_book"}),r.a.createElement(p.a.Column,{title:"\u603b\u9898\u6570",dataIndex:"count",sortable:!0}),r.a.createElement(p.a.Column,{title:"uva",dataIndex:"uva"}),r.a.createElement(p.a.Column,{title:"HDU",dataIndex:"hdu"}),r.a.createElement(p.a.Column,{title:"POJ",dataIndex:"poj"}),r.a.createElement(p.a.Column,{title:"cf",dataIndex:"cf"}),r.a.createElement(p.a.Column,{title:"bc",dataIndex:"bc"}),r.a.createElement(p.a.Column,{title:"\u72b6\u6001",dataIndex:"user.status",cell:this.renderState}))}},{key:"render",value:function e(){return r.a.createElement("div",null,r.a.createElement("div",{className:"page-header"},r.a.createElement("div",{className:"page-header-title"},"\u505a\u9898\u7edf\u8ba1",r.a.createElement("small",null,"\u4e0a\u6b21\u66f4\u65b0: 3\u5c0f\u65f6\u524d"))),r.a.createElement("hr",null),r.a.createElement("div",{className:"search-header"},r.a.createElement(c.a,{onChange:this.onSerchChange,onSearch:this.onSearch,placeholder:"\u641c\u7d22"}),r.a.createElement("div",{className:"buttons"},r.a.createElement(u.a,{onClick:this.setDataSourceAll,className:"button"},"\u67e5\u770b\u5168\u90e8"),r.a.createElement(u.a,{type:"primary",onClick:this.setDataSourceNow},"\u53ea\u770b\u73b0\u5f79"))),this.tableRender(),r.a.createElement(i.a,{style:k.pagination,shape:"arrow-only",current:this.state.current,onChange:this.handlePagination,total:this.state.dataSource.length,pageSize:this.state.pageSize,pageSizeSelector:"dropdown",pageSizePosition:"start",onPageSizeChange:this.handlePageSizeChange,pageSizeList:[30,50,100,150]}))}}]),t}(a.Component);N.displayName="ProblemsTable";var k={pagination:{margin:"20px 0",textAlign:"center"},circleGreen:{display:"inline-block",background:"#28a745",width:"8px",height:"8px",borderRadius:"50px",marginRight:"4px"},stateTextGreen:{color:"#28a745"}},_=N,V=n(933);function F(e){return(F="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function e(t){return typeof t}:function e(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(e)}function T(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function W(e,t){for(var n=0;n<t.length;n++){var a=t[n];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}function z(e,t,n){return t&&W(e.prototype,t),n&&W(e,n),e}function D(e,t){return!t||"object"!==F(t)&&"function"!=typeof t?B(e):t}function B(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function R(e){return(R=Object.setPrototypeOf?Object.getPrototypeOf:function e(t){return t.__proto__||Object.getPrototypeOf(t)})(e)}function A(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&M(e,t)}function M(e,t){return(M=Object.setPrototypeOf||function e(t,n){return t.__proto__=n,t})(e,t)}var U=function(e){function t(){return T(this,t),D(this,R(t).apply(this,arguments))}return A(t,e),z(t,[{key:"render",value:function e(){return r.a.createElement("div",{className:"problems-container"},r.a.createElement(_,null))}}]),t}(r.a.Component),L=t.default=U},709:function(e,t,n){n(709),e.exports=n(916)},915:function(e,t,n){n(709),n(709),e.exports=n(918)},916:function(e,t,n){n(269),n(700),n(186),n(40),n(917)},917:function(e,t,n){},918:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a,r=o(n(919));function o(e){return e&&e.__esModule?e:{default:e}}t.default=r.default,e.exports=t.default},919:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e},r,o,i,l=E(n(0)),u,s=E(n(1)),c,f=E(n(3)),p=n(701),d=E(p),h,y=E(n(126)),m,b=E(n(39)),v=n(27),g,S=E(n(920));function E(e){return e&&e.__esModule?e:{default:e}}function w(e,t){for(var n=Object.getOwnPropertyNames(t),a=0;a<n.length;a++){var r=n[a],o=Object.getOwnPropertyDescriptor(t,r);o&&o.configurable&&void 0===e[r]&&Object.defineProperty(e,r,o)}return e}function I(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function O(e,t){var n={};for(var a in e)t.indexOf(a)>=0||Object.prototype.hasOwnProperty.call(e,a)&&(n[a]=e[a]);return n}function x(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function C(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function P(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):w(e,t))}var j=(o=r=function(e){function t(n,a){x(this,t);var r=C(this,e.call(this,n,a)),o=null;return n.filter&&n.filter.length&&(n.filter.forEach(function(e){e.default&&(o=e.value)}),null===o&&(o=n.filter[0].value)),r.state={filterValue:o,key:r.props.value||n.defaultValue||""},r}return P(t,e),t.prototype.componentWillReceiveProps=function e(t){var n=null;t.filter&&t.filter.length&&this.props.filter!==t.filter&&(t.filter.forEach(function(e){e.default&&(n=e.value)}),null===n&&(n=t.filter[0].value),this.setState({filterValue:n})),t.hasOwnProperty("value")&&this.setState({key:t.value})},t.prototype.onChange=function e(t){t in this.props||this.setState({key:t});var n={key:t,filter:this.state.filterValue,filterValue:this.state.filterValue};this.props.onSearch(n)},t.prototype.onInputUpdate=function e(t){this.setState({key:t}),this.props.onChange(t)},t.prototype.onInputEnter=function e(){this.onSearch()},t.prototype.onFilter=function e(t){this.setState({filterValue:t});var n={key:this.state.key,filterValue:t};this.props.onFilterChange(t,n)},t.prototype.onSearch=function e(){this.props.onSearch({filter:this.state.filterValue,filterValue:this.state.filterValue,key:this.state.key})},t.prototype.onInputBlur=function e(t){var n={key:this.state.key,filter:this.state.filterValue,filterValue:this.state.filterValue};this.props.onInputBlur(t,n)},t.prototype.onInputFocus=function e(t,n){var a={key:this.state.key,filter:this.state.filterValue,filterValue:this.state.filterValue};this.props.onInputFocus(t,n,a)},t.prototype.render=function e(){var t,n=this.props,r=n.filter,o=n.type,i=n.searchIcon,u=n.hasIcon,s=n.autoWidth,c=n.className,h=n.style,m=n.filterAutoWidth,g=O(n,["filter","type","searchIcon","hasIcon","autoWidth","className","style","filterAutoWidth"]),E=this.props,w=E.size,x=E.dataSource,C=E.searchText,P=E.combox,j=E.overlayVisible,N=E.inputWidth,k=u;void 0!==i&&(k=i,v.log.deprecated("searchIcon","hasIcon","Search"));var _=this.context.prefix||this.props.prefix,V=(0,f.default)((I(t={},_+"search",!0),I(t,_+"search-"+o,o),I(t,w,!0),I(t,"auto-width",s),I(t,c,c),t)),F=(0,f.default)(I({},_+"icon-alone",!C)),T=a({},g);return l.default.createElement("div",{className:V,style:h},l.default.createElement("div",{className:_+"search-lt"},r.length>0?l.default.createElement(d.default,{shape:"arrow-only",className:"filter",autoWidth:m,value:this.state.filterValue,onChange:this.onFilter.bind(this)},r.map(function(e,t){return l.default.createElement("div",{value:e.value,key:t},e.text)})):null,P?l.default.createElement(S.default,a({},T,{overlay:P,width:N,placeholder:this.props.placeholder,value:this.state.key,overlayVisible:j,onChange:this.onChange.bind(this),onInputEnter:this.onSearch.bind(this),onInputUpdate:this.onInputUpdate.bind(this),onInputFocus:this.onInputFocus.bind(this),onInputBlur:this.onInputBlur.bind(this)})):l.default.createElement("div",{className:_+"search-lt-input",style:{width:N,float:"left"}},l.default.createElement(p.Combobox,a({},T,{shape:"arrow-only",hasArrow:!1,placeholder:this.props.placeholder,value:this.state.key,dataSource:x,onChange:this.onChange.bind(this),onInputEnter:this.onInputEnter.bind(this),onInputUpdate:this.onInputUpdate.bind(this),onInputFocus:this.onInputFocus.bind(this),onInputBlur:this.onInputBlur.bind(this)})))),l.default.createElement("div",{className:_+"search-rt"},l.default.createElement(y.default,{type:"normal"===this.props.type?"normal":"primary",size:w,onClick:this.onSearch.bind(this)},k?l.default.createElement(b.default,{type:"search",className:F}):""," ",C)))},t}(l.default.Component),r.propTypes={prefix:s.default.string,size:s.default.string,filter:s.default.array,searchIcon:s.default.bool,hasIcon:s.default.bool,searchText:s.default.string,combox:s.default.node,inputWidth:s.default.oneOfType([s.default.string,s.default.number]),overlayVisible:s.default.bool,dataSource:s.default.array,type:s.default.oneOf(["primary","secondary","normal"]),value:s.default.oneOfType([s.default.string,s.default.number]),defaultValue:s.default.string,className:s.default.string,placeholder:s.default.string,onInputFocus:s.default.func,onInputBlur:s.default.func,onSearch:s.default.func,onChange:s.default.func,onFilterChange:s.default.func,autoWidth:s.default.bool,filterAutoWidth:s.default.bool,style:s.default.object,container:s.default.any},r.defaultProps={prefix:"next-",type:"primary",size:"medium",filter:[],dataSource:[],inputWidth:"auto",hasIcon:!0,combox:!1,searchText:"Search",autoWidth:!1,filterAutoWidth:!0,onChange:function e(){},onSearch:function e(){},onInputFocus:function e(){},onInputBlur:function e(){},onFilterChange:function e(){}},r.contextTypes={prefix:s.default.string},o);j.displayName="Search",t.default=j,e.exports=t.default},920:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e},r,o,i=n(0),l=y(i),u,s=y(n(1)),c,f=y(n(17)),p,d=y(n(85)),h=n(27);function y(e){return e&&e.__esModule?e:{default:e}}function m(e,t){for(var n=Object.getOwnPropertyNames(t),a=0;a<n.length;a++){var r=n[a],o=Object.getOwnPropertyDescriptor(t,r);o&&o.configurable&&void 0===e[r]&&Object.defineProperty(e,r,o)}return e}function b(e,t){var n={};for(var a in e)t.indexOf(a)>=0||Object.prototype.hasOwnProperty.call(e,a)&&(n[a]=e[a]);return n}function v(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function g(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function S(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):m(e,t))}var E=f.default.findDOMNode,w=(o=r=function(e){function t(n){v(this,t);var a=g(this,e.call(this,n));return a.state={placeholder:a.props.placeholder||"",visible:a.props.overlayVisible,value:a.props.value||""},a}return S(t,e),t.prototype.componentDidMount=function e(){this.setInputWidth()},t.prototype.componentWillReceiveProps=function e(t){this.setState({visible:t.overlayVisible,value:t.value,placeholder:t.placeholder})},t.prototype.onInputChange=function e(t){var n=t.target.value;this.props.onInputUpdate(n)},t.prototype.onInputKeyDown=function e(t){13===t.keyCode&&this.props.onInputEnter(t)},t.prototype.onInputFocus=function e(t){this.props.onInputFocus(t)},t.prototype.onInputBlur=function e(t){this.props.onInputBlur(t)},t.prototype.setInputWidth=function e(){var t=E(this.refs.target);this._inputWidth=t.clientWidth+16+"px"},t.prototype.render=function e(){var t=this,n=this.state.visible,r=this.props,o=r.overlay,i=r.width,u=r.container,s=b(r,["overlay","width","container"]);return l.default.createElement("div",{className:"search-custom",style:{width:i},ref:"custom"},l.default.createElement("input",a({},(0,h.pickAttrs)(s),{ref:"target",placeholder:this.state.placeholder,value:this.state.value,onChange:this.onInputChange.bind(this),onFocus:this.onInputFocus.bind(this),onKeyDown:this.onInputKeyDown.bind(this),onBlur:this.onInputBlur.bind(this)})),l.default.createElement(d.default,{visible:n,autoFocus:!1,ref:"overlay",safeNode:function e(){return t.refs.custom},target:function e(){return t},onOpen:this.afterOpen,container:u},l.default.createElement("div",{style:{width:"auto"===i?this._inputWidth:i}},o)))},t}(i.Component),r.propTypes={placeholder:s.default.string,value:s.default.string,overlayVisible:s.default.bool,overlay:s.default.any,width:s.default.oneOfType([s.default.string,s.default.number]),onInputUpdate:s.default.func,onInputEnter:s.default.func,onInputFocus:s.default.func,onInputBlur:s.default.func,container:s.default.any},r.defaultProps={overlay:null},o);w.displayName="Combox",t.default=w,e.exports=t.default},932:function(e,t,n){},933:function(e,t,n){}}]);