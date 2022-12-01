// // Json , Api And Ajax Code Section
// /**
//  Config info
//  */
//     //After publishing, it will be changed to the main address of the domain.
//  let baseUrl = 'http://127.0.0.1:8000/'
//
// /**
//  ============== Form Section ================
//  */
// //
// // function getFormInput() {
// //     return {
// //         first_name: $('input[name =Fname]').val(),
// //         last_name: $('input[name =lname]').val(),
// //         father_name: $('input[name =father_name]').val(),
// //         birth: $('input[name =birth]').val(),
// //         national_code: $('input[name =Ncode]').val(),
// //         national_card_series: $('input[name =series_Ncard]').val(),
// //         birthcertificate_number: $('input[name =id_number]').val(),
// //         birthcertificate_serial: $('input[name =id_serial]').val(),
// //         birthcertificate_series: $('input[name =id_series]').val(),
// //         issued: $('input[name =registration]').val(),
// //         state: $('input[name =state]').val(),
// //         city: $('input[name =city]').val(),
// //         store_address: $('input[name =store_address]').val(),
// //         zipcode_pos: $('input[name =poscod_pos]').val(),
// //         store_phone: $('input[name =store_phone]').val(),
// //         business_license_number: $('input[name =business_num]').val(),
// //         tax_code: $('input[name =tax_code]').val(),
// //         senf: $('input[name =senf]').val(),
// //         mobile: $('input[name =storephone]').val(),
// //         substrate: $('select[name =substrate_type]').val(),
// //         ownership: $('select[name =ownership_type]').val(),
// //         leaseterm_from: $('input[name =lease_from]').val(),
// //         leaseterm_to: $('input[name =lease_until]').val(),
// //         introducer_name: $('input[name =identifier_fname]').val(),
// //         introducer_lastname: $('input[name =identifier_lname]').val(),
// //         introducer_phone: $('input[name =identifier_phone]').val(),
// //         introducer_address: $('input[name =identifier_address]').val(),
// //         first_account_number: $('input[name =first_accountNum]').val(),
// //         first_bank_name: $('select[name =first_bankName]').val(),
// //         first_shaba_number: $('input[name =first_shaba_code]').val(),
// //         second_account_number: $('input[name =secand_accountNum]').val(),
// //         second_bank_name: $('select[name =second_bankName]').val(),
// //         second_shaba_number: $('input[name =second_shaba_code]').val(),
// //         paziresh: $('input[name =paziresh]').val(),
// //         businesslicense: $('input[name =image_permission]').val(),
// //         leaseterm: $('input[name =image_lease]').val(),
// //         ownership_document: $('input[name =image_owership]').val(),
// //         birthcertificate: $('input[name =image]').val(),
// //         front_nationalcard: $('input[name =image_onNaCard]').val(),
// //         back_nationalcard: $('input[name =image_BackNaCard]').val(),
// //         signatureseal: $('input[name =image_sign]').val(),
// //         sabin_form_first: $('input[name =image_sabin1]').val(),
// //         sabin_form_second: $('input[name =image_sabin2]').val(),
// //     }
// // }
// // function setInput(pos){
// //     setValue("Fname",pos.title)
// //     setValue("lname",pos.id)
// //
// //     // setValue("Fname",  pos.first_name);
// //     //  setValue("lname",  pos.last_name);
// //     // setValue("father_name",  pos.father_name);
// //     // setValue("birth",   pos.birth);
// //     // setValue("Ncode",   pos.national_code);
// //     // setValue("series_Ncard",  pos.national_card_series);
// //     // setValue("id_number",  pos.birthcertificate_number);
// //     // setValue("id_serial",   pos.birthcertificate_serial);
// //     // setValue("id_series",  pos.birthcertificate_series);
// //     // setValue("issued",   pos.issued);
// //     // setValue("state",  pos.state);
// //     // setValue("city",   pos.city);
// //     // setValue("store_address",   pos.store_address);
// //     // setValue("poscode_pos",  pos.zipcod_pos);
// //     // setValue("store_phone",  pos.store_phone);
// //     // setValue("business_num",   pos.business_license_number);
// //     // setValue("tax_code",   pos.tax_code);
// //     // setValue("senf",   pos.senf);
// //     // setValue("storephone",   pos.mobile);
// //     // setValue("substrate_type",   pos.substrate);
// //     // setValue("ownership_type",   pos.ownership);
// //     // setValue("lease_from",   pos.leaseterm_from);
// //     // setValue("lease_until",   pos.leaseterm_to);
// //     // setValue("identifier_fname",   pos.introducer_name);
// //     //    setValue("identifier_lname",   pos.introducer_lastname);
// //     //    setValue("identifier_phone",   pos.introducer_phone);
// //     //    setValue("identifier_address",   pos.introducer_address);
// //     //    setValue("first_accountNum",   pos.first_account_number);
// //     //    setValue("first_bankName",   pos.first_bank_name);
// //     //    setValue("first_shaba_code",   pos.first_shaba_number);
// //     //    setValue("secand_accountNum",   pos.second_account_number);
// //     //    setValue("second_bankName",   pos.second_bank_name);
// //     //    setValue("second_shaba_code",   pos.second_shaba_number);
// //     //    setValue("paziresh",   pos.paziresh);
// //     //    setValue("image_permission",   pos.businesslicense);
// //     //    setValue("image_lease",   pos.leaseterm);
// //     //    setValue("image_owership",   pos.ownership_document);
// //     //    setValue("image",   pos.birthcertificate);
// //     //    setValue("image_onNaCard",   pos.front_nationalcard);
// //     //    setValue("image_BackNaCard",   pos.back_nationalcard);
// //     //    setValue("image_sign",   pos.signatureseal);
// //     //    setValue("image_sabin1",   pos.sabin_form_first);
// //     //    setValue("image_sabin2",   pos.sabin_form_second);
// // }
// //
// // /**
// //  ================ public =================
// //  */
// //
// // function setValue(  name ,value){
// //    document.getElementsByName(name).values= value
// // }
// //
// // function changePage(href) {
// //     window.location.href = baseUrl + href;
// // }
// //
// // function handleAjaxError(error) {
// //   displayError(error);
// //
// //   switch (error.status) {
// //     case 404:
// //       console.log(error.responseText);
// //       toastr["error"]("صفحه مورد نظر یافت نشد!", "خطا")
// //       break;
// //     case 500:
// //       console.log(error.responseText);
// //       break;
// //     default:
// //       console.log(error);
// //       break;
// //   }
// // }
// //
// // /**
// //  ================ Search Box =================
// //  */
// // let statusCode
// // let WebXmlHttpRequest=(method, url,data)=>{
// //     return fetch(url, {
// //         method: method,
// //         body: JSON.stringify(data),
// //         headers: data ? {'Content-Type': 'application/json'} : {}
// //     }).then(function (res) {
// //         //status massaged
// //         statusCode = res.status;
// //         return res.json();
// //     }).catch(function (err) {
// //         if (err.message === 'Failed to fetch'){
// //             toastr["error"]("مشکل در برقراری ارتباط با سرور!", "خطا")
// //         }
// //         console.log(err)
// //     })
// // }
// // let vm = {
// //     "list" : [],
// //     "mode" : "list"
// // }
// //
// // let getPage = document.getElementById("pos-list")
// // let editBtn = document.getElementsByClassName('edit-btn')
// // let item=""
// // function getPosList(){
// //     WebXmlHttpRequest("GET","https://jsonplaceholder.typicode.com/posts" ).then(function (res) {
// //         res.map(function(elem){
// //             item+= `
// //                     <div class="container card-body pos-card  mt-3">
// //                         <div class="row">
// //                             <div class="col-md-6  mt-3 mt-md-0">
// //                                 <label class="card-title">نام: </label>
// //                                 <p class="card-text">${elem.id} </p>
// //                             </div>
// //                             <div class="col-md-6  mt-3 mt-md-0">
// //                                 <label class="card-title">نام خانوادگی: </label>
// //                                 <p class="card-text">${elem.userId} </p>
// //                             </div>
// //                         </div>
// //                         <div class="row">
// //                             <div class="col-md-6  mt-3 mt-md-0">
// //                                 <label class="card-title"> تاریخ ثبت درخواست: </label>
// //                                 <p class="card-text">${elem.title}</p>
// //                             </div>
// //                             <div class="col-md-6  mt-3 mt-md-0">
// //                                 <label class="card-title"> وضعیت: </label>
// //                                 <p class="card-text staus "> ${elem.body} </p>
// //                             </div>
// //                         </div>
// //                         <div class="row">
// //                             <div class="col-md-12  mt-3 mt-md-0 pos-btn-group">
// //                                 <a class="btn btn-success card-btn-edit edit-btn" href="#" onclick="getPosRequest(this)"><i class="bi bi-pencil-square"></i>
// //                                     ويرايش درخواست </a>
// //                             </div>
// //                              <span name="pk" hidden> ${elem.id} </span>
// //                         </div>
// //                     </div>
// //                      `
// //         })
// //         document.getElementById('pos-list').innerHTML=item
// //         if(statusCode===200){
// //             // toastr["success"]("", "درخواست شما با موفقیت ثبت شد.")
// //         }
// //     })
// // }
// // function getPosRequest(requestID){
// //      vm.mode = "edit";
// //     let pk = Number(requestID.parentElement.parentElement.lastElementChild.innerHTML)
// //      WebXmlHttpRequest("GET", 'https://jsonplaceholder.typicode.com/posts/'+ pk +'/').then(function (res) {
// //          setInput(res)
// //          changePage('PosRequestForm.html/')
// //
// //      }).catch(function (err) {
// //          handleAjaxError(err)
// //      })
// // }
// // if(getPage){
// //     getPage.addEventListener("click",getPosList())
// //
// // }
// //
// //
// // /**
// //  * PosRequest form
// //  */
// //
// //
// // const posForm = document.querySelector('#pos-form')
// // function postForm(e){
// //     e.preventDefault();
// //     let data = getFormInput()
// //     WebXmlHttpRequest("POST","https://jsonplaceholder.typicode.com/posts",data ).then(function (res) {
// //         if(statusCode===201){
// //             toastr["success"]("", "درخواست شما با موفقیت ثبت شد.")
// //             changePage('PosRequestShow.html/')
// //         }
// //     }).catch(function (err) {
// //         console.log("error")
// //         console.log(err)
// //         console.log("error")
// //     })
// // }
// // function putForm(pk){
// //
// //     WebXmlHttpRequest("PUT", 'https://jsonplaceholder.typicode.com/posts/'+ pk +'/').then(function(res){
// //         changePage('khadamatik_group/PosRequestForm.html')
// //     //     return res
// //     //
// //     }).catch(function(err){
// //         console.log(err)
// //     })
// // }
// //
// // if (posForm){
// //     posForm.addEventListener('submit', (vm)=>{
// //          if (vm.mode === "add") {
// //           postForm()
// //              console.log("add")
// //         } else if (vm.mode === "edit") {
// //           putForm();
// //         }
// //     })
// // }
// //  function add(){
// //     vm.mode="add"
// //  }
// //
// //
// //
// //
// //
// //
//
//
//
// //
// //
// // $('form#pos-form').submit(function(e){
// //     e.preventDefault();
// //     let first_name = $('input[name =Fname]').val()
// //     let last_name = $('input[name =lname]').val()
// //     let father_name = $('input[name =father_name]').val()
// //     let birth = $('input[name =birth]').val()
// //     let Ncode = $('input[name =Ncode]').val()
// //     let series_Ncard = $('input[name =series_Ncard]').val()
// //     let id_number = $('input[name =id_number]').val()
// //     let id_serial = $('input[name =id_serial]').val()
// //     let id_series = $('input[name =id_series]').val()
// //     let registration = $('input[name =registration]').val()
// //     let state = $('input[name =state]').val()
// //     let city = $('input[name =city]').val()
// //     let store_address = $('input[name =store_address]').val()
// //     let poscod_pos = $('input[name =poscod_pos]').val()
// //     let store_phone = $('input[name =store_phone]').val()
// //     let business_num = $('input[name =business_num]').val()
// //     let tax_code = $('input[name =tax_code]').val()
// //     let senf = $('input[name =senf]').val()
// //     let storephone = $('input[name =storephone]').val()
// //     let substrate_type = $('select[name =substrate_type]').val()
// //     let ownership_type = $('select[name =ownership_type]').val()
// //     let lease_from = $('input[name =lease_from]').val()
// //     let lease_until = $('input[name =lease_until]').val()
// //     let identifier_fname = $('input[name =identifier_fname]').val()
// //     let identifier_lname = $('input[name =identifier_lname]').val()
// //     let identifier_phone = $('input[name =identifier_phone]').val()
// //     let identifier_address = $('input[name =identifier_address]').val()
// //     let first_accountNum = $('input[name =first_accountNum]').val()
// //     let first_bankName = $('select[name =first_bankName]').val()
// //     let first_shaba_code = $('input[name =first_shaba_code]').val()
// //     let secand_accountNum = $('input[name =secand_accountNum]').val()
// //     let second_bankName = $('select[name =second_bankName]').val()
// //     let second_shaba_code = $('input[name =second_shaba_code]').val()
// //     let paziresh = $('input[name =paziresh]').val()
// //     let image_permission = $('input[name =image_permission]').val()
// //     let image_lease = $('input[name =image_lease]').val()
// //     let image_owership = $('input[name =image_owership]').val()
// //     let image = $('input[name =image]').val()
// //     let image_onNaCard = $('input[name =image_onNaCard]').val()
// //     let image_BackNaCard = $('input[name =image_BackNaCard]').val()
// //     let image_sign = $('input[name =image_sign]').val()
// //     let image_sabin1 = $('input[name =image_sabin1]').val()
// //     let image_sabin2 = $('input[name =image_sabin2]').val()
// //     let url=$('form#pos-form').attr('action')
// //     let tt= { userId: first_name,
// //         title: last_name,
// //         body: father_name}
// //     $.ajax({
// //         url: url,
// //         type : 'POST',
// //         data : JSON.stringify(tt)/*{
// //             userId: first_name,
// //             title: last_name,
// //             body: father_name,
// // birth:birth,
// // national_code:Ncode,
// // national_card_series:series_Ncard,
// // birthcertificate_number: id_number,
// // birthcertificate_serial:id_serial,
// // birthcertificate_series:id_series,
// // issued:registration,
// // state:state,
// // city:city,
// // store_address:store_address,
// // zipcode_pos:poscod_pos,
// // store_phone:store_phone,
// // business_license_number:business_num,
// // tax_code:tax_code,
// // senf:senf,
// // mobile:storephone,
// // substrate:substrate_type,
// // ownership:ownership_type,
// // leaseterm_from:lease_from,
// // leaseterm_to:lease_until,
// // introducer_name:identifier_fname,
// // introducer_lastname:identifier_lname,
// // introducer_phone:identifier_phone,
// // introducer_address:identifier_address,
// // first_account_number:first_accountNum,
// // first_bank_name:first_bankName,
// // first_shaba_number:first_shaba_code,
// // second_account_number:secand_accountNum ,
// // second_bank_name:second_bankName,
// // second_shaba_number:second_shaba_code,
// // paziresh:paziresh,
// // businesslicense:image_permission,
// // leaseterm:image_lease,
// // ownership_document:image_owership,
// // birthcertificate:image,
// // front_nationalcard:image_onNaCard,
// // back_nationalcard:image_BackNaCard,
// // signatureseal:image_sign,
// // sabin_form_first:image_sabin1,
// // sabin_form_second:image_sabin2,
// // status : 'ثبت درخواست'
// // }*/,
// //         success: function (response) {
// //             console.log(response)
// //             if(response===201){
// //                 // toster.success("درخواست با موفقیت ثبت شد", 'Turtle Bay Resort', {timeOut: 5000})
// //                 console.log(response)
// //             }else if(response!=201){
// //                 console.log("Error")
// //             }
// //         }
// //     })
// // })
// //
//
//
//
//
// /* const search = document.querySelector('#search-box');
//  const result = document.querySelector('#result');
//  const posList = document.querySelector('#pos-list');
//
//  search.addEventListener("keyup",handle);
//
//  async function handle() {
//      const find = encodeURIComponent(this.value);
//      const responseData = await  fetch("./public/response.json" + find);
//      const responses =  await responseData.json();
//      let html = "";
//      if (responses.length){
//          for (let book of books) {
//              html += `
//                   <div class="container card-body pos-card  mt-3">
//                      <div class="row">
//                          <div class="col-md-6  mt-3 mt-md-0">
//                              <label class="card-title">نام: </label>
//                              <p class="card-text">${elem.id} </p>
//                          </div>
//                          <div class="col-md-6  mt-3 mt-md-0">
//                              <label class="card-title">نام خانوادگی: </label>
//                              <p class="card-text">${elem.userId} </p>
//                          </div>
//                      </div>
//                      <div class="row">
//                          <div class="col-md-6  mt-3 mt-md-0">
//                              <label class="card-title"> تاریخ ثبت درخواست: </label>
//                              <p class="card-text">${elem.title}</p>
//                          </div>
//                          <div class="col-md-6  mt-3 mt-md-0">
//                              <label class="card-title"> وضعیت: </label>
//                              <p class="card-text staus "> ${elem.body} </p>
//                          </div>
//                      </div>
//                      <div class="row">
//                          <div class="col-md-12  mt-3 mt-md-0 pos-btn-group">
//                              <a class="btn btn-success card-btn-edit " href="#"><i class="bi bi-pencil-square"></i>
//                                  ويرايش درخواست </a>
//                          </div>
//                      </div>
//                  </div>
//              `;
//          }
//          posList.innerHTML = html;
//      }else {
//          posList.innerHTML = "";
//          result. innerHTML= " موردی یافت نشد"
//
//
//      }
//  }
//
//  */
//
// // const posForm = document.querySelector("form")
// /* let getPage = document.getElementById("pos-list")
// let postForm = document.querySelector("#pos-form")
// let item= ""
// let WebXmlHttpRequest =(method, url,data) => {
//     // whit fetch
//     return fetch(url, {
//         method: method,
//         body: JSON.stringify(data),
//         headers: data ? {"Content-Type": "application/"} : {}
//     }).then(function (res) {
//         return res.json()
//     }).catch(function (err) {
//         console.log(err)
//     })
// }
// */
//
//
// //     //whihe promise
// //    /*  return new Promise((resolve, reject)=> {
// //             let xHttp = new XMLHttpRequest()
// //             xHttp.open(method, url)
// //             xHttp.responseType = "json"
// //             if(data){
// //                 xHttp.setRequestHeader("Content-Type","application/json")
// //             }
// //             xHttp.onload=()=>{
// //                 resolve(xHttp.response)
// //             }
// //             xHttp.onerror=()=> {
// //                 reject("error")
// //             }
// //             xHttp.send(JSON.stringify(data))
// //         }) */
// // }
// /*
//     function get() {
//         WebXmlHttpRequest("GET", "https://jsonplaceholder.typicode.com/posts").then(function (res) {
//             res.map(function (elem) {
//                 item += `
//                      <div class="container card-body pos-card  mt-3">
//                         <div class="row">
//                             <div class="col-md-6  mt-3 mt-md-0">
//                                  <label class="card-title">نام: </label>
//                                  <p class="card-text">${elem.id} </p>
//                              </div>
//                              <div class="col-md-6  mt-3 mt-md-0">
//                                  <label class="card-title">نام خانوادگی: </label>
//                                  <p class="card-text">${elem.userId} </p>
//                              </div>
//                          </div>
//                          <div class="row">
//                              <div class="col-md-6  mt-3 mt-md-0">
//                                  <label class="card-title"> تاریخ ثبت درخواست: </label>
//                                  <p class="card-text">${elem.title}</p>
//                              </div>
//                              <div class="col-md-6  mt-3 mt-md-0">
//                                  <label class="card-title"> وضعیت: </label>
//                                  <p class="card-text staus "> ${elem.body} </p>
//                              </div>
//                          </div>
//                          <div class="row">
//                              <div class="col-md-12  mt-3 mt-md-0 pos-btn-group">
//                                  <a class="btn btn-success card-btn-edit " href="#"><i class="bi bi-pencil-square"></i>
//                                     ويرايش درخواست </a>
//                              </div>
//                          </div>
//                      </div>
//
//                         `
//                 document.getElementById('pos-list').innerHTML = item
//             })
//
//         })
//
//         //whihe promise
//         /*
//             WebXmlHttpRequest("GET","https://jsonplaceholder.typicode.com/posts" ).then(function (res) {
//                 res.map(function(elem){
//                     item+= `
//                         <div class="container card-body pos-card  mt-3">
//                             <div class="row">
//                                 <div class="col-md-6  mt-3 mt-md-0">
//                                     <label class="card-title">نام: </label>
//                                     <p class="card-text">${elem.id} </p>
//                                 </div>
//                                 <div class="col-md-6  mt-3 mt-md-0">
//                                     <label class="card-title">نام خانوادگی: </label>
//                                     <p class="card-text">${elem.userId} </p>
//                                 </div>
//                             </div>
//                             <div class="row">
//                                 <div class="col-md-6  mt-3 mt-md-0">
//                                     <label class="card-title"> تاریخ ثبت درخواست: </label>
//                                     <p class="card-text">${elem.title}</p>
//                                 </div>
//                                 <div class="col-md-6  mt-3 mt-md-0">
//                                     <label class="card-title"> وضعیت: </label>
//                                     <p class="card-text staus "> ${elem.body} </p>
//                                 </div>
//                             </div>
//                             <div class="row">
//                                 <div class="col-md-12  mt-3 mt-md-0 pos-btn-group">
//                                     <a class="btn btn-success card-btn-edit " href="#"><i class="bi bi-pencil-square"></i>
//                                         ويرايش درخواست </a>
//                                 </div>
//                             </div>
//                         </div>
//
//                            `
//                 })
//                  document.getElementById('pos-list').innerHTML=item
//             }).catch(function (err) {
//                 console.log(err)
//             })
//    }
//          */
//
//
// /* function post() {
//      // preventDefault();
//      let first_name = document.querySelector('#Fname').values
//      let last_name = document.querySelector('#lname').values
//      let father_name = document.querySelector('#father_name').values
//      let birth = document.querySelector('#birth').values
//      let Ncode = document.querySelector('#Ncode').values
//      let series_Ncard = document.querySelector('#series_Ncard').values
//      let id_number = document.querySelector('#id_number').values
//      let id_serial = document.querySelector('#id_serial').values
//      let id_series = document.querySelector('#id_series').values
//      let registration = document.querySelector('#registration').values
//      let state = document.querySelector('#state').values
//      let city = document.querySelector('#city').values
//      let store_address = document.querySelector('#store_address').values
//      let poscod_pos = document.querySelector('#poscod_pos').values
//      let store_phone = document.querySelector('#store_phone').values
//      let business_num = document.querySelector('#business_num').values
//      let tax_code = document.querySelector('#tax_code').values
//      let senf = document.querySelector('#senf').values
//      let storephone = document.querySelector('#storephone').values
//      let substrate_type = document.querySelector('#substrate_type').values
//      let ownership_type = document.querySelector('#ownership_type').values
//      let lease_from = document.querySelector('#lease_from').values
//      let lease_until = document.querySelector('#lease_until').values
//      let identifier_fname = document.querySelector('#identifier_fname').values
//      let identifier_lname = document.querySelector('#identifier_lname').values
//      let identifier_phone = document.querySelector('#identifier_phone').values
//      let identifier_address = document.querySelector('#identifier_address').values
//      // let first_accountNum = document.querySelector('#first_accountNum').values
//      let first_bankName = document.querySelector('#first_bankName').values
//      let first_shaba_code = document.querySelector('#first_shaba_code').values
//      let secand_accountNum = document.querySelector('#secand_accountNum').values
//      let second_bankName = document.querySelector('#second_bankName').values
//      let second_shaba_code = document.querySelector('#second_shaba_code').values
//      let paziresh = document.querySelector('#paziresh').values
//      let image_permission = document.querySelector('#image_permission').values
//      let image_lease = document.querySelector('#image_lease').values
//      let image_owership = document.querySelector('#image_owership').values
//      let image = document.querySelector('#image').values
//      let image_onNaCard = document.querySelector('#image_onNaCard').values
//      let image_BackNaCard = document.querySelector('#image_BackNaCard').values
//      let image_sign = document.querySelector('#image_sign').values
//      let image_sabin1 = document.querySelector('#image_sabin1').values
//      let image_sabin2 = document.querySelector('#image_sabin2').values
//      let data = {
//          userId: 4,
//          title: "fdghfhfj",
//          body: 564564576,
//          // birth:birth,
//          // national_code:Ncode,
//          // national_card_series:series_Ncard,
//          // birthcertificate_number: id_number,
//          // birthcertificate_serial:id_serial,
//          // birthcertificate_series:id_series,
//          // issued:registration,
//          // state:state,
//          // city:city,
//          // store_address:store_address,
//          // zipcode_pos:poscod_pos,
//          // store_phone:store_phone,
//          // business_license_number:business_num,
//          // tax_code:tax_code,
//          // senf:senf,
//          // mobile:storephone,
//          // substrate:substrate_type,
//          // ownership:ownership_type,
//          // leaseterm_from:lease_from,
//          // leaseterm_to:lease_until,
//          // introducer_name:identifier_fname,
//          // introducer_lastname:identifier_lname,
//          // introducer_phone:identifier_phone,
//          // introducer_address:identifier_address,
//          // first_account_number:first_accountNum,
//          // first_bank_name:first_bankName,
//          // first_shaba_number:first_shaba_code,
//          // second_account_number:secand_accountNum ,
//          // second_bank_name:second_bankName,
//          // second_shaba_number:second_shaba_code,
//          // paziresh:paziresh,
//          // businesslicense:image_permission,
//          // leaseterm:image_lease,
//          // ownership_document:image_owership,
//          // birthcertificate:image,
//          // front_nationalcard:image_onNaCard,
//          // back_nationalcard:image_BackNaCard,
//          // signatureseal:image_sign,
//          // sabin_form_first:image_sabin1,
//          // sabin_form_second:image_sabin2
//      }
//      console.log(data)
//      WebXmlHttpRequest("POST", "https://jsonplaceholder.typicode.com/posts", data).then(function (res) {
//          console.log(res)
//      }).catch(function (err) {
//          console.log(err)
//      })
//  }
// */
// //whihe promise
// /*
// WebXmlHttpRequest("POST","https://jsonplaceholder.typicode.com/posts",data).then(function (res) {
//     console.log(res)
// }).catch(function (err) {
//     console.log(err)
// })
//
//  */
//
//
// // getPage.addEventListener("click", get)
// // postForm.addEventListener("click", post)
//
// // $('form#pos-form').submit(function(e){
// //     e.preventDefault()
// //     let first_name = $('input[name=Fname]').val();
// //     let last_name = $('input[name=lname]').val();
// //     let father_name = $('input[name=father_name]').val();
// //     let birth = $('input[name=birth]').val();
// //     let Ncode = $('input[name=Ncode]').val();
// //     let series_Ncard = $('input[name=series_Ncard]').val();
// //     let id_number = $('input[name=id_number]').val();
// //     let id_serial = $('input[name=id_serial]').val();
// //     let id_series = $('input[name=id_series]').val();
// //     let registration = $('input[name=registration]').val();
// //     let state = $('input[name=state]').val();
// //     let city = $('input[name=city]').val();
// //     let store_address = $('input[name=store_address]').val();
// //     let poscod_pos = $('input[name=poscod_pos]').val();
// //     let store_phone = $('input[name=store_phone]').val();
// //     let business_num = $('input[name=business_num]').val();
// //     let tax_code = $('input[name=tax_code]').val();
// //     let senf = $('input[name=senf]').val();
// //     let storephone = $('input[name=storephone]').val();
// //     let substrate_type = $('select[name=substrate_type]').val();
// //     let ownership_type = $('select[name=ownership_type]').val();
// //     let lease_from = $('input[name=lease_from]').val();
// //     let lease_until = $('input[name=lease_until]').val();
// //     let identifier_fname = $('input[name=identifier_fname]').val();
// //     let identifier_lname = $('input[name=identifier_lname]').val();
// //     let identifier_phone = $('input[name=identifier_phone]').val();
// //     let identifier_address = $('input[name=identifier_address]').val();
// //     let first_accountNum = $('input[name=first_accountNum]').val();
// //     let first_bankName = $('select[name=first_bankName]').val();
// //     let first_shaba_code = $('input[name=first_shaba_code]').val();
// //     let secand_accountNum = $('input[name=secand_accountNum]').val();
// //     let second_bankName = $('select[name=second_bankName]').val();
// //     let second_shaba_code = $('input[name=second_shaba_code]').val();
// //     let paziresh = $('input[name=paziresh]').val();
// //     let image_permission = $('input[name=image_permission]').val();
// //     let image_lease = $('input[name=image_lease]').val();
// //     let image_owership = $('input[name=image_owership]').val();
// //     let image = $('input[name=image]').val();
// //     let image_onNaCard = $('input[name=image_onNaCard]').val();
// //     let image_BackNaCard = $('input[name=image_BackNaCard]').val();
// //     let image_sign = $('input[name=image_sign]').val();
// //     let image_sabin1 = $('input[name=image_sabin1]').val();
// //     let image_sabin2 = $('input[name=image_sabin2]').val();
// //     let url = $('form#pos-form').attr('action');
// //     $.ajax({
// //         type: 'POST',
// //         url: url,
// //         data:{
// //             first_name:first_name,
// //             last_name:last_name,
// //             father_name:father_name,
// //             birth:birth,
// //             national_code:Ncode,
// //             national_card_series:series_Ncard,
// //             birthcertificate_number: id_number,
// //             birthcertificate_serial:id_serial,
// //             birthcertificate_series:id_series,
// //             issued:registration,
// //             state:state,
// //             city:city,
// //             store_address:store_address,
// //             zipcode_pos:poscod_pos,
// //             store_phone:store_phone,
// //             business_license_number:business_num,
// //             tax_code:tax_code,
// //             senf:senf,
// //             mobile:storephone,
// //             substrate:substrate_type,
// //             ownership:ownership_type,
// //             leaseterm_from:lease_from,
// //             leaseterm_to:lease_until,
// //             introducer_name:identifier_fname,
// //             introducer_lastname:identifier_lname,
// //             introducer_phone:identifier_phone,
// //             introducer_address:identifier_address,
// //             first_account_number:first_accountNum,
// //             first_bank_name:first_bankName,
// //             first_shaba_number:first_shaba_code,
// //             second_account_number:secand_accountNum ,
// //             second_bank_name:second_bankName,
// //             second_shaba_number:second_shaba_code,
// //             paziresh:paziresh,
// //             businesslicense:image_permission,
// //             leaseterm:image_lease,
// //             ownership_document:image_owership,
// //             birthcertificate:image,
// //             front_nationalcard:image_onNaCard,
// //             back_nationalcard:image_BackNaCard,
// //             signatureseal:image_sign,
// //             sabin_form_first:image_sabin1,
// //             sabin_form_second:image_sabin2
// //         },
// //         success: function (response) {
// //             console.log(response)
// //         }
// //     })
// // })
//
//
//
//
//
// // JavaScript And JQuery Code Section
//
// document.addEventListener('DOMContentLoaded', () => {
//     "use strict";
//
//     /**
//      * Persian DateTime Picker
//      */
//     jalaliDatepicker.startWatch();
//
//     /**
//      * Preloader
//      */
//     const preloader = document.querySelector('#preloader');
//     if (preloader) {
//         window.addEventListener('load', () => {
//             preloader.remove();
//         });
//     }
//
//     /**
//      * Upload file
//      */
//     $(function() {
//         // We can attach the `fileselect` event to all file inputs on the page
//         $(document).on('change', ':file', function() {
//             var input = $(this),
//                 numFiles = input.get(0).files ? input.get(0).files.length : 1,
//                 label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
//             input.trigger('fileselect', [numFiles, label]);
//         });
//
//         // We can watch for our custom `fileselect` event like this
//         $(document).ready( function() {
//             $(':file').on('fileselect', function(event, numFiles, label) {
//
//                 var input = $(this).parents('.input-group').find(':text'),
//                     log = numFiles > 1 ? numFiles + ' files selected' : label;
//
//                 if( input.length ) {
//                     input.val(log);
//                 } else {
//                     if( log ) alert(log);
//                 }
//
//             });
//         });
//
//     });
// })