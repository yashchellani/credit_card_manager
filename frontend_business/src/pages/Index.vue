<template>
  <q-page class="" style="background-color:#f2f2f2">
    
    <!-- metrics row -->
    <div class="row">
      <div class="col-4 q-pa-md">
        <!-- Total Credit loaned -->
        <div class="bg-white shadow-5  text-black q-pl-md" style="border-radius:15px">
          <div class="flex justify-between items-center no-wrap">
            <div class="">
              <div class="">Total Credit Loaned</div>
      
                <div class="font-size-32 font-600 ">$
                  <animated-number
                  :value="'230210'"
                  :formatValue="formatToPrice"
                  :duration="1500"
                /></div>

               
                <div class="myTextGrey font-size-16"><span class="text-green">+55% </span> since last month</div>
            </div>

            <div class="q-mr-sm">
              <!-- <q-icon name="credit_card" size="lg"></q-icon> -->
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="height:120px" />
            </div>
              
          </div>
        </div>
      </div>

      <div class="col-4 q-pa-md">
        <!-- Total Credit loaned -->
        <div class="bg-white shadow-5 q-pl-md text-black" style="border-radius:15px">
          <div class="flex justify-between items-center no-wrap">
            <div class="">
              <div class="">Number of Users</div>
      
                <div class="font-size-32 font-600 ">
                  <animated-number
                  :value="'3150'"
                  :formatValue="formatToPrice"
                  :duration="1500"
                /></div>

               
                <div class="myTextGrey font-size-16"><span class="text-green">+18% </span> since last month</div>
            </div>

            <div class="q-mr-md">
              <!-- <q-icon name="account_circle" size="lg"></q-icon> -->
              <Lottie :options="defaultOptions2"  v-on:animCreated="handleAnimation" style="height:120px" />
            </div>
              
          </div>
        </div>
      </div>

      <div class="col-4 q-pa-md">
        <!-- Total Credit loaned -->
        <div class="bg-white shadow-5 q-pl-md text-black" style="border-radius:15px">
          <div class="flex justify-between items-center no-wrap">
            <div class="">
              <div class="">Interest Earned</div>
      
                <div class="font-size-32 font-600 ">$
                  <animated-number
                  :value="'4604.2'"
                  :formatValue="formatToPrice"
                  :duration="1500"
                /></div>

               
                <div class="myTextGrey font-size-16"><span class="text-green">+18% </span> since last month</div>
            </div>

            <div class="" style="padding-top:10px;padding-bottom:10px">
              <!-- <q-icon name="account_circle" size="lg"></q-icon> -->
              <Lottie :options="defaultOptions3"  v-on:animCreated="handleAnimation" style="height:100px;" />
            </div>
              
          </div>
        </div>
      </div>

    </div>


    
    <div class="row q-mb-lg">

      <!-- LEFT SIDE -->
      <div class="col-4  q-px-md q-pt-sm ">
        <highcharts
             :options="pieChartOptions" 
            class="shadow-5" 
            style="border-radius:15px"
          />

        <!-- transactions -->
        <div class="q-mt-lg q-pt-md shadow-5 bg-white " style="border-radius:15px">
          <div class="flex justify-between items-start q-mx-md" style="color:#67748e">
            <div class="font-400 font-size-20 q-mb-md text-black" >Suspicious Transactions</div>
            <q-icon name="receipt_long" size="md" class="text-white"></q-icon>
          </div>
          

          <div class=" q-ml-md q-mb-sm font-600" style="color:#67748e">NEWEST</div>
          <q-list>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-415646 (User #148)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$2,500</div>
              </q-item-section>
            </q-item>
 <q-separator ></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-415649 (User #148)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 10:30am</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$2,000</div>
              </q-item-section>
            </q-item>
             <q-separator ></q-separator>

            <div class=" q-ml-md q-mt-md q-mb-sm font-600" style="color:#67748e">YESTERDAY</div>

            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-411846 (User #92)</q-item-label>
                <q-item-label class="myTextGrey" >26 August 2022, at 8:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-green font-500">+$18,500</div>
              </q-item-section>
            </q-item>
 <q-separator ></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-355646 (User #131)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 4:00pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-green font-500">+$1,200</div>
              </q-item-section>
            </q-item>
             <q-separator ></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-114646 (User #13)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:30pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                <div class="text-red font-500">-$1,142.30</div>
              </q-item-section>
            </q-item>
             <q-separator ></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-334643 (User #2130)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 12:00pm</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$1,444.90</div>
              </q-item-section>
            </q-item>

             <q-separator ></q-separator>
            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label class="font-500 text-black">#MS-6124646 (User #1318)</q-item-label>
                <q-item-label class="myTextGrey" >27 August 2022, at 11:00am</q-item-label>
              </q-item-section>

              <q-item-section side >
                
                <div class="text-red font-500">-$15,554.90</div>
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
              <span style="font-size:14px; color:#4f5051" class="">{{chartDate}}</span><br/>
              <span style=" font-size:30px; font-weight:600;color:#4f5051" > User Growth: </span> 
              
              <b><span  style="font-size:28px;color:black;font-weight:500" >{{chartValue}} Users</span></b>
          </div>

        </div>

        <!-- bottom right table  -->
        <q-table
      title="Feedback & Issues"
      :data="data"
      :columns="columns"
      row-key="name"
      class="q-mt-lg shadow-5 q-pt-sm q-pb-md"
      style="border-radius:15px"
      :rows-per-page-options="[7]"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="name" :props="props">
            {{ props.row.name }}
          </q-td>
          <q-td key="User" :props="props">

            <q-badge color="orange">
              {{ props.row.User }}
            </q-badge>
          </q-td>
          <q-td key="Feedback" :props="props">
           
              {{ props.row.Feedback }}
           
          </q-td>
          <q-td key="Status" :props="props">
            <q-badge color="green">
              {{ props.row.Status }}
            </q-badge>
          </q-td>
         
        </q-tr>
      </template>
    </q-table>

        
      </div>


    </div>



  </q-page>
</template>

<script>
import {Chart} from 'highcharts-vue'
import AnimatedNumber from "animated-number-vue";
import Lottie from 'vue-lottie';
import * as animationData from './creditCard.json';
import * as animationData2 from './people.json';
import * as animationData3 from './money.json';
export default {
   components: {
    highcharts: Chart,
    AnimatedNumber,
    Lottie
  },
  data () {
    return {
      chartDate:'',
      chartTab:'Spending',
      chartValue:'',
       chartOptions: {
        chart: {
          backgroundColor: "white",
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
          //  gridLineColor: "#454444",
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
               [1646092800000,698],
              [1648771200000,510], 
              [1651363200000,887],
              [1654041600000,712],
              [1656633600000,1011],
              [1659312000000,1111],
              
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

      pieChartOptions:{
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Overall Customer Spending Pattern'
        },
        credits: {
          enabled: false,
        },
        // subtitle: {
        //     text: 'Click the slices to view versions. Source: <a href="http://statcounter.com" target="_blank">statcounter.com</a>'
        // },

        accessibility: {
            announceNewData: {
                enabled: true
            },
            point: {
                valueSuffix: '%'
            }
        },

        plotOptions: {
            series: {
                dataLabels: {
                    enabled: true,
                    format: '{point.name}: {point.y:.1f}%'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:12px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },

        series: [
            {
                name: "Browsers",
                colorByPoint: true,
                data: [
                    {
                        name: "Food & Drinks",
                        y: 25,
                        // drilldown: "Chrome"
                    },
                    {
                        name: "Utility Bills",
                        y: 31,
                        // drilldown: "Firefox"
                    },
                    {
                        name: "Transport",
                        y: 16,
                        // drilldown: "Internet Explorer"
                    },
                    {
                        name: "Leisure",
                        y: 17,
                        // drilldown: "Safari"
                    },
                 
                    {
                        name: "Other",
                        y: 11,
                        // drilldown: null
                    }
                ]
            }
        ],
        // drilldown: {
        //     series: [
        //         {
        //             name: "Chrome",
        //             id: "Chrome",
        //             data: [
        //                 [
        //                     "v65.0",
        //                     0.1
        //                 ],
        //                 [
        //                     "v64.0",
        //                     1.3
        //                 ],
        //                 [
        //                     "v63.0",
        //                     53.02
        //                 ],
        //                 [
        //                     "v62.0",
        //                     1.4
        //                 ],
        //                 [
        //                     "v61.0",
        //                     0.88
        //                 ],
        //                 [
        //                     "v60.0",
        //                     0.56
        //                 ],
        //                 [
        //                     "v59.0",
        //                     0.45
        //                 ],
        //                 [
        //                     "v58.0",
        //                     0.49
        //                 ],
        //                 [
        //                     "v57.0",
        //                     0.32
        //                 ],
        //                 [
        //                     "v56.0",
        //                     0.29
        //                 ],
        //                 [
        //                     "v55.0",
        //                     0.79
        //                 ],
        //                 [
        //                     "v54.0",
        //                     0.18
        //                 ],
        //                 [
        //                     "v51.0",
        //                     0.13
        //                 ],
        //                 [
        //                     "v49.0",
        //                     2.16
        //                 ],
        //                 [
        //                     "v48.0",
        //                     0.13
        //                 ],
        //                 [
        //                     "v47.0",
        //                     0.11
        //                 ],
        //                 [
        //                     "v43.0",
        //                     0.17
        //                 ],
        //                 [
        //                     "v29.0",
        //                     0.26
        //                 ]
        //             ]
        //         },
        //         {
        //             name: "Firefox",
        //             id: "Firefox",
        //             data: [
        //                 [
        //                     "v58.0",
        //                     1.02
        //                 ],
        //                 [
        //                     "v57.0",
        //                     7.36
        //                 ],
        //                 [
        //                     "v56.0",
        //                     0.35
        //                 ],
        //                 [
        //                     "v55.0",
        //                     0.11
        //                 ],
        //                 [
        //                     "v54.0",
        //                     0.1
        //                 ],
        //                 [
        //                     "v52.0",
        //                     0.95
        //                 ],
        //                 [
        //                     "v51.0",
        //                     0.15
        //                 ],
        //                 [
        //                     "v50.0",
        //                     0.1
        //                 ],
        //                 [
        //                     "v48.0",
        //                     0.31
        //                 ],
        //                 [
        //                     "v47.0",
        //                     0.12
        //                 ]
        //             ]
        //         },
        //         {
        //             name: "Internet Explorer",
        //             id: "Internet Explorer",
        //             data: [
        //                 [
        //                     "v11.0",
        //                     6.2
        //                 ],
        //                 [
        //                     "v10.0",
        //                     0.29
        //                 ],
        //                 [
        //                     "v9.0",
        //                     0.27
        //                 ],
        //                 [
        //                     "v8.0",
        //                     0.47
        //                 ]
        //             ]
        //         },
        //         {
        //             name: "Safari",
        //             id: "Safari",
        //             data: [
        //                 [
        //                     "v11.0",
        //                     3.39
        //                 ],
        //                 [
        //                     "v10.1",
        //                     0.96
        //                 ],
        //                 [
        //                     "v10.0",
        //                     0.36
        //                 ],
        //                 [
        //                     "v9.1",
        //                     0.54
        //                 ],
        //                 [
        //                     "v9.0",
        //                     0.13
        //                 ],
        //                 [
        //                     "v5.1",
        //                     0.2
        //                 ]
        //             ]
        //         },
        //         {
        //             name: "Edge",
        //             id: "Edge",
        //             data: [
        //                 [
        //                     "v16",
        //                     2.6
        //                 ],
        //                 [
        //                     "v15",
        //                     0.92
        //                 ],
        //                 [
        //                     "v14",
        //                     0.4
        //                 ],
        //                 [
        //                     "v13",
        //                     0.1
        //                 ]
        //             ]
        //         },
        //         {
        //             name: "Opera",
        //             id: "Opera",
        //             data: [
        //                 [
        //                     "v50.0",
        //                     0.96
        //                 ],
        //                 [
        //                     "v49.0",
        //                     0.82
        //                 ],
        //                 [
        //                     "v12.1",
        //                     0.14
        //                 ]
        //             ]
        //         }
        //     ]
        // }
      },
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },
      defaultOptions2:{
        animationData: animationData2.default,
        loop:true,
        autoplay:true
      },
      defaultOptions3:{
        animationData: animationData3.default,
        loop:true,
        autoplay:true
      },
      animationSpeed: 1.5,

      columns: [
        {
          name: 'name',
          required: true,
          label: 'Feedback Id',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'User', align: 'center', label: 'User', field: 'User', sortable: true },
        { name: 'Feedback',align: 'center', label: 'Feedback', field: 'Feedback' },
        { name: 'Status', align: 'center',label: 'Status', field: 'Status' },

      ],

      data: [
        {
          name: '#F-156',
          User: 'User #119',
          Feedback: 'I have issues with my card, please help',
          Status: 'Replied',
        },
        {
          name: '#F-1315',
          User: 'User #1254',
          Feedback: 'I accidentally paid, what do I do?',
          Status: 'Replied',
        },
        {
          name: '#F-1091',
          User: 'User #119',
          Feedback: 'I made a false payment, how to rollback?',
          Status: 'Replied',
        },
        {
          name: '#F-30112',
          User: 'User #3022',
          Feedback: 'I have issues with my card, please help',
          Status: 'Replied',
        },
        {
          name: '#F-1245',
          User: 'User #99',
          Feedback: 'How to sign up another card?',
          Status: 'Replied',
        },
        {
          name: '#F-13456',
          User: 'User #12',
          Feedback: 'I have issues with my card, please help',
          Status: 'Replied',
        },
        {
          name: '#F-13456',
          User: 'User #1235',
          Feedback: 'I have issues with my card, please help',
          Status: 'Replied',
        },
        
  
      ]
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
    formatToPrice(item) {
      return `<span>${parseFloat(Number(item).toFixed(0)).toLocaleString('en')}</span>`;
    },
    handleAnimation: function (anim) {
        this.anim = anim;
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
