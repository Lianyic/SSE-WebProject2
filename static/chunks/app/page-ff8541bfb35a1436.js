(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[931],{2431:function(){},5072:function(e,s,r){Promise.resolve().then(r.bind(r,6990))},6990:function(e,s,r){"use strict";r.r(s),r.d(s,{default:function(){return y}});var t=r(7437),i=r(3706),a=r(1021),n=r(5943),l=r(8584),o=r(7466),c=r(5945),u=r(4480),d=r(9551),h=r(9376);let{Title:m,Text:g}=i.default;function y(){let e=(0,h.useRouter)(),s=async s=>{try{await d.Z.post("/user/login",s),a.ZP.success("Login successful"),e.push("/analysis")}catch(e){a.ZP.error("Login failed. Please check your credentials.")}},r=async e=>{try{await d.Z.post("/user/register",e),a.ZP.success("Registration successful"),await s(e)}catch(e){a.ZP.error("Registration failed. Please try again.")}},i=[{key:"login",label:"Login",children:(0,t.jsxs)(n.Z,{onFinish:s,layout:"vertical",children:[(0,t.jsx)(n.Z.Item,{name:"username",rules:[{required:!0,message:"Please enter your username"}],children:(0,t.jsx)(l.Z,{placeholder:"Username",size:"large"})}),(0,t.jsx)(n.Z.Item,{name:"password",rules:[{required:!0,message:"Please enter your password"}],children:(0,t.jsx)(l.Z.Password,{placeholder:"Password",size:"large"})}),(0,t.jsx)(o.ZP,{type:"primary",htmlType:"submit",size:"large",block:!0,children:"Login"})]})},{key:"register",label:"Register",children:(0,t.jsxs)(n.Z,{onFinish:r,layout:"vertical",children:[(0,t.jsx)(n.Z.Item,{name:"username",rules:[{required:!0,message:"Please enter your username"}],children:(0,t.jsx)(l.Z,{placeholder:"Username",size:"large"})}),(0,t.jsx)(n.Z.Item,{name:"password",rules:[{required:!0,message:"Please enter your password"}],children:(0,t.jsx)(l.Z.Password,{placeholder:"Password",size:"large"})}),(0,t.jsx)(o.ZP,{type:"primary",htmlType:"submit",size:"large",block:!0,children:"Register"})]})}];return(0,t.jsx)("div",{style:{display:"flex",justifyContent:"center",alignItems:"center",backgroundColor:"#f0f2f5",padding:"20px"},children:(0,t.jsxs)(c.Z,{style:{maxWidth:400,width:"100%",borderRadius:"10px",boxShadow:"0 4px 8px rgba(0, 0, 0, 0.1)"},children:[(0,t.jsxs)("div",{style:{textAlign:"center",marginBottom:"20px"},children:[(0,t.jsx)(m,{level:3,style:{marginBottom:0,color:"#1890ff"},children:"Welcome to DreamAI"}),(0,t.jsx)(g,{type:"secondary",children:"Unlock insights with your dreams"})]}),(0,t.jsx)(u.Z,{defaultActiveKey:"login",items:i,centered:!0})]})})}},9551:function(e,s,r){"use strict";var t=r(3464);r(6600);let i=t.Z.create({baseURL:"http://127.0.0.1:5000/api",withCredentials:!0});s.Z=i}},function(e){e.O(0,[73,512,971,117,744],function(){return e(e.s=5072)}),_N_E=e.O()}]);