<template>
  <q-page class="" style="">
    
    

    <div class="row">
      <div class="col-4  q-px-md q-pt-sm ">
        <!-- card div -->
        <div class="cardStyle shadow-5" style="width:100%; height:250px;z-index:0 !important;position: relative;">
            <div class="mask bg-gradient-dark" style="z-index:1 !important;"></div>
            

            <!-- wifi div and card number -->
            <div class=" q-pa-md flex column justify-between no-wrap" style="z-index:2 !important;height:100%;position: relative;">
              <div class="">
                <div class="flex justify-between items-center q-mb-md">
                  <q-icon name="wifi" color="white" size="sm" class=""></q-icon>
                  <img src="~assets/pomona.png" alt="" style="width:125px">
                </div>
                
                <div class="font-500 font-size-20" style="color:white">4562   1122   4594   7852</div>
              </div>


              <!-- card holder + logo -->
              <div class="text-white flex justify-between items-center " style="width:100%">
                
                <div class="flex">
                  <div class="q-mr-md">
                    <div class="font-size-12 text-grey">Card Holder</div>
                    <div class="font-size-16">Greg G Tan</div>
                  </div>
                  

                  <div class="">
                    <div class="font-size-12 text-grey">Expires</div>
                    <div class="font-size-16">10/25</div>
                  </div>
                </div>

                <div class="flex items-center">
                  <img src="~assets/goldman_white.png" alt="" style="width:50px;" class="q-mr-md"/>
                   <img src="~assets/master.png" alt="" style="width:50px">
                   

                </div>
                 
              </div>
              



            </div>


        </div>

        <!-- transactions -->
        <div class="q-mt-md q-pt-md shadow-5 myGrey" style="border-radius:15px">
          <div class="flex justify-between items-start q-mx-md" style="color:#67748e">
            <div class="font-600 font-size-20 q-mb-md text-white" >Your Transactions</div>
            <q-icon name="receipt_long" size="md" class="text-white"></q-icon>
          </div>
          

          <div class=" q-ml-md q-mb-sm font-600" style="color:#67748e">NEWEST</div>
          <q-list>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Netflix</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$2,500</div>
              </q-item-section>
            </q-item>
 <q-separator dark></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Apple</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 10:30am</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$2,000</div>
              </q-item-section>
            </q-item>
             <q-separator dark></q-separator>

            <div class=" q-ml-md q-mt-md q-mb-sm font-600" style="color:#67748e">YESTERDAY</div>

            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Salary</q-item-label>
                <q-item-label class="myTextGrey" >26 August 2022, at 8:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-green font-500">+$18,500</div>
              </q-item-section>
            </q-item>
 <q-separator dark></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Stripe</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 4:00pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-green font-500">+$1,200</div>
              </q-item-section>
            </q-item>
             <q-separator dark></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Shopee</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                <div class="text-red font-500">-$12.30</div>
              </q-item-section>
            </q-item>
             <q-separator dark></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Grab</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:00pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$14.90</div>
              </q-item-section>
            </q-item>

             <q-separator dark></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Ya Kun Kaya Toast</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 11:00am</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$14.90</div>
              </q-item-section>
            </q-item>

            <q-separator dark></q-separator>

            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500">Web Flow</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 10:30am</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="font-500 text-white">Pending</div>
              </q-item-section>
            </q-item>

           

            
          </q-list>




        </div>

      </div>


      <div class="col-8 q-px-md q-pt-sm">
        <!-- graph -->
        <div class="shadow-5" style="position:relative;border-radius:15px">
           <highcharts
            :constructorType="'stockChart'" :options="chartOptions" 
            class="roundedDiv" ref="topChart"
            style="border-radius:15px"
          />
          
          <div class="" style="position:absolute;right:24px; top:18px">
          <!-- <q-tabs
          
            v-model="chartTab"
            dense
            no-caps
            indicator-color="blue-4"
            active-color="blue-4"
            @click="topChartTabChange()"
            > 
              <q-tab  :ripple="false" name="Spending" label="Spending"  />
              <q-tab  :ripple="false" name="Savings" label="Savings" />
              <q-tab  :ripple="false" name="Premium" label="Premium" />
              
        
            </q-tabs> -->
          </div>

          <div  class="" style="position:absolute; top:10px; left:17px">
              <span style="font-size:14px;color:white;">{{chartDate}}</span><br/>
              <span style=" font-size:30px; font-weight:600;color:#7cb5ec" > {{chartTab}}: </span> 
              
              <b><span  style="font-size:28px;color:white;font-weight:500" >${{chartValue}}</span></b>
          </div>

        </div>

        <!-- bottom right divs  -->
        <div class="row q-mt-md">
          <!-- invoice div -->
          <div class="col-12 q-py-md q-pr-md ">
            <div class="shadow-5 q-pa-md myGrey" style="border-radius:15px">
                <div class="flex justify-between items-start q-mx-md" style="color:#67748e">
                  <div class="font-600 font-size-20 q-mb-md text-white" >Your Invoices</div>
                  <q-btn outline color="primary" label="View All"></q-btn>
                </div>
              
                <q-list>
                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">27 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16">$180.19</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>


                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">25 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$591.10</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>


                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">21 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$127.12</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">10 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$510.76</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">19 July, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$3,180</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">10 July, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$1,400</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                 
                 

                  
                </q-list>



            
            
            </div>

          </div>


          <!-- <div class="col-6 q-py-md q-pl-md">
            <div class="shadow-5 q-pa-md myGrey" style="border-radius:15px">
                <div class="flex justify-between items-start q-mx-md" style="color:#67748e">
                  <div class="font-600 font-size-20 q-mb-md text-white" >Your Invoices</div>
                  <q-btn outline color="primary" label="View All"></q-btn>
                </div>
              
                <q-list>
                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">27 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$180.19</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>


                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">25 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$591.10</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>


                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">21 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$127.12</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item> 
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">10 August, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$510.76</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">19 July, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$3,180</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                  <q-separator dark></q-separator>

                  <q-item >
                    <q-item-section>
                      <q-item-label class="font-500">10 July, 2022</q-item-label>
                      <q-item-label class="myTextGrey" >#MS-415646</q-item-label>
                    </q-item-section>

                    <q-item-section side  >
                      <div class="flex items-center">
                        <div class="q-mr-sm font-size-16 ">$1,400</div>
                        <q-btn flat color="primary" icon-right="download" label="PDF"  />
                      </div>
                      
                    </q-item-section>
                  </q-item>
                 
                 

                  
                </q-list>



            
            
            </div>

          </div> -->
        </div>

        
      </div>


    </div>




  </q-page>
</template>

<script>
import {Chart} from 'highcharts-vue'
export default {
   components: {
    highcharts: Chart,
  },
  data () {
    return {
      chartDate:'',
      chartTab:'Spending',
      chartValue:'',
       chartOptions: {
        chart: {
          backgroundColor: "#08101a",
          spacingTop: 100,
          events: {
            // //start at 3 months ago 
            //  load() {
            //       let startDate = new Date()
            //       startDate.setMonth(startDate.getMonth()-1)
            //       let endDate = Date.now()
                  
            //       this.xAxis[0].setExtremes(startDate,endDate)
            //   }
          }
        },
        // xAxis: {
        //     categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        // },
        yAxis: {
          tickAmount: 4,
           gridLineColor: "#454444",
        },
        tooltip: {
          split: false,
          // backgroundColor:'#4f7591',
          style:{
            color:'black'
          },
          valueDecimals: 4,
          xDateFormat:'',
           pointFormat: '<span style="font-family:Roboto; font-weight:600;color:#7cb5ec;">{series.name}: </span> <b><span style="font-family:Roboto;font-weight:500">${point.y} </span></b>',
          
        },
         //to remove inactivity
        plotOptions: {
          series: {
            states: {
              inactive: {
                opacity: 0.8
              }
            }
          }
        },

        credits: {
          enabled: false,
        },
        navigator: {
          enabled: true,
          height: 50,
          margin:50,
          // maskFill: 'rgba(31, 255, 171, 0.1)'
          
        },
        scrollbar: {
          enabled: false,
        },
        rangeSelector:{
          buttons:[
            {
            type:'month',
            count:1,
            text:'1m',
            title:'View 1 Month'
            },
            {
            type:'month',
            count:3,
            text:'3m',
            title:'View 3 Months'
            },
            {
            type:'month',
            count:6,
            text:'6m',
            title:'View 6 Months'
            },
            {
            type:'year',
            count:1,
            text:'1y',
            title:'View 1 Year'
            },
            {
            type:'all',
            text:'All',
            title:'View All'
            },
          
          
          ],
          buttonTheme: { // styles for the buttons
            fill: 'none',
            stroke: 'none',
            'stroke-width': 0,
            r: 5,
            // style: {
            //     color: 'black',
            //     fontWeight: 'bold'
            // },
            // states: {
            //     hover: {
            //       fill: 'rgb(107, 107, 107,0.5)',
            //       color:'black'
            //     },
            //     select: {
            //         fill: '#1fffab',
            //         style: {
                        
            //         }
            //     }
                
            // },
          },
          //pushing the range and dates down to bottom to make space for big words
          floating: true,
          y: -155,
          verticalAlign: 'bottom',

          inputStyle: {
          // color: '#1fffab',
          fontWeight: 'bold'
          },

          inputBoxBorderColor: 'gray',
          inputBoxWidth: 100,
          inputBoxHeight: 18,
          
        },
        
        series: [{
           name: "Spending",
            // color:'#1fffab',
            point:{
              events:{
                mouseOver:(e)=>{
                  // console.log(e)
                  let newDate = new Date(e.target.x)
                  this.chartDate = this.getFormattedDate(newDate)

                  // console.log(e.target.y)
                  
                  this.chartValue = parseFloat(e.target.y.toFixed(4)).toLocaleString('en') 
                  
                }
              }
            },
            data: [
               [1646092800000,8329.9],
              [1648771200000,15129.9], 
              [1651363200000,20029.29],
              [1654041600000,8001.93],
              [1656633600000,12129.81],
              [1659312000000,5329.12],
              // [1656006015000,329.9],
              // [1653902942000,329.9],
              // [1656650094000,329.9],
              // [1652743322000,329.9],
              // [1658547020000,329.9],
              // [1658168417000,329.9],
              // [1651504127000,329.9],
              
              ]
              }
            ]
        
        //  series: [
        //   {
        //     name: "Bitcoin",
        //     pointInterval: 24 * 3600 * 1000,
        //      color:'#1fffab',
        //     point:{
        //       events:{
        //         mouseOver:(e)=>{
        //           // console.log(e)
        //           let newDate = new Date(e.target.x)
        //           this.bottomChartDate = this.getFormattedDate(newDate)

        //           // console.log(e.target.y)
                  
        //           this.bottomChartValue = parseFloat(e.target.y.toFixed(4)).toLocaleString('en') 
                  
        //         }
        //       }
        //     },
        //     data: [
  
              
        //     ],
        //   },


        // ],
      },

      chartOptions2:{
        tooltip: {
            formatter: function () {
                return 'The value for <b>' + this.x +
                    '</b> is <b>' + this.y + '</b>';
            }
        },
        xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },

        series: [{
            data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        }, {
            data: [194.1, 95.6, 54.4, 29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4]
        }]
      }


    }
  },
  mounted(){
    let currDate = new Date()
    this.chartDate = this.getFormattedDate(currDate)
    this.chartValue = this.chartOptions.series[0].data.at(-1)[1]
  },  
  methods:{
    getFormattedDate(today){
      var week = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
      var month = new Array('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July','Aug','Sep','Oct','Nov','Dec');
      var day  = week[today.getDay()]
      var dd   = today.getDate();
      var mm   = month[today.getMonth()] //January is 0!
      var yyyy = today.getFullYear();
      var hour = today.getHours();
      var minu = today.getMinutes();

      if(dd<10)  { dd='0'+dd } 
  
      if(minu<10){ minu='0'+minu } 

      return day+' - '+mm+' '+dd+' '+yyyy+', '+hour+':'+minu;
    },
    getFormattedDateNoTime(today){
      var week = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
      var month = new Array('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July','Aug','Sep','Oct','Nov','Dec');
      var day  = week[today.getDay()]
      var dd   = today.getDate();
      var mm   = month[today.getMonth()] //January is 0!
      var yyyy = today.getFullYear();
      var hour = today.getHours();
      var minu = today.getMinutes();

      if(dd<10)  { dd='0'+dd } 
  
      if(minu<10){ minu='0'+minu } 

      return day+' - '+mm+' '+dd+' '+yyyy
    },
  }
}
</script>

<style lang="scss">

.cardStyle{
  background-image:url('../assets/curved.jpg');
  background-size: cover;
  background-position: 50%;
  
  position:relative;
  overflow:hidden;
  width:100%;
  height:100%;
  border-radius:15px;
}


.mask {
    position: absolute;
    background-size: cover;
    background-position: 50%;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: .8;
    z-index:0 !important;

}

.bg-gradient-dark {
    background-image: linear-gradient(310deg,#141727,#3a416f);
    width:100%;
    height:100%;
    z-index:0 !important;
}
.cardInnerStyle{
  // position:relative;
  z-index:2;
  
}
</style>
