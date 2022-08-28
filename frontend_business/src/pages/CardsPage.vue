<template>
    <q-page class="q-pa-md">
        <div class="row">
            <div class="col-12 bg-white q-py-sm q-px-md " style="border-radius:15px">
                
                <div class="flex justify-between">
                    <div class="" style="width:70%">
                    
                        <div class="font-500 font-size-22">Overall Credit Balance</div>
                        <div class="q-mt-md font-size-18">Positive Credit</div>
                        <q-linear-progress :value="0.7" class="q-mb-sm" color="positive" />

                        <div class="q-mt-lg font-size-18">Neutral Credit</div>
                        <q-linear-progress :value="0.2" class="q-mb-sm" />

                        <div class="q-mt-lg font-size-18">Negative Credit</div>
                        <q-linear-progress :value="0.1" class="q-mb-sm" color="negative" />

                        
                    </div>
                    

                    <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:250px;" />
                </div>
                
            </div>




            <div class="col-12">
                <q-table
                title="New Applications"
                :data="data"
                :columns="columns"
                row-key="name"
                class="q-mt-lg shadow-5 q-pt-sm q-pb-md"
                style="border-radius:15px"
                :rows-per-page-options="[5]"
                >
                <template v-slot:body="props">
                    <q-tr :props="props">
                    <q-td key="name" :props="props">
                        <q-badge color="orange">
                            {{ props.row.name }}
                        </q-badge>
                        
                    </q-td>
                   
                    <q-td key="Name" :props="props">
                    
                        {{ props.row.Name }}
                    
                    </q-td>
                    <q-td key="Email" :props="props">
                    
                        {{ props.row.Email }}
                    
                    </q-td>
                    <q-td key="Gender" :props="props">
                    
                        {{ props.row.Gender }}
                    
                    </q-td>
                    <q-td key="Marital_Status" :props="props">
                    
                        {{ props.row.Marital_Status }}
                    
                    </q-td>
                    <q-td key="Address" :props="props">
                    
                        {{ props.row.Address }}
                    
                    </q-td>
                    <q-td key="Number" :props="props">
                    
                        {{ props.row.Number }}

                    </q-td>
                    <q-td key="DOB" :props="props">
                    
                        {{ props.row.DOB }}
                    
                    </q-td>
                    <q-td key="Credit_Score" :props="props">
                    
                        {{ props.row.Credit_Score }}
                    
                    </q-td>
                    <q-td key="Status" :props="props">
                        
                        {{ props.row.Status }}
                        
                    </q-td>
                    <q-td key="Application_Status" :props="props">
                        <q-badge color="grey" v-if="props.row.Application_Status == 'Pending'">
                            {{ props.row.Application_Status }}
                        </q-badge>
                        <q-badge color="red" v-else>
                            {{ props.row.Application_Status }}
                        </q-badge>
                    </q-td>
                    <q-td key="button" :props="props">
                        <q-btn label="Issue Credit Card" color="primary" outline></q-btn>
                    </q-td>


                    
                    </q-tr>
                </template>
                </q-table>
            </div>


            <div class="col-12">
                <q-table
                title="Existing Cards"
                :data="data2"
                :columns="columns2"
                row-key="name"
                class="q-mt-lg shadow-5 q-pt-sm q-pb-md"
                style="border-radius:15px"
                :rows-per-page-options="[5]"
                >
                <template v-slot:body="props">
                    <q-tr :props="props">
                    <q-td key="name" :props="props">
                        <q-badge color="orange">
                            {{ props.row.name }}
                        </q-badge>
                        
                    </q-td>
                   
                    <q-td key="Name" :props="props">
                    
                        {{ props.row.Name }}
                    
                    </q-td>
                    <q-td key="Email" :props="props">
                    
                        {{ props.row.Email }}
                    
                    </q-td>
                    <q-td key="Card_Type" :props="props">
                    
                        {{ props.row.Card_Type }}
                    
                    </q-td>
                    <q-td key="Credit_Balance" :props="props">
                        <q-badge color="red" v-if="props.row.Credit_Balance.charAt(0) ==  '('">
                            {{ props.row.Credit_Balance }}
                        </q-badge>
                        <q-badge color="grey" v-else-if="props.row.Credit_Balance.charAt(0) ==  '0'">
                            {{ props.row.Credit_Balance }}
                        </q-badge>
                        <q-badge color="green" v-else>
                            {{ props.row.Credit_Balance }}
                        </q-badge>
                    
                       
                    
                    </q-td>
                    <q-td key="Date_Created" :props="props">
                    
                        {{ props.row.Date_Created }}
                    
                    </q-td>
  

                    
                    </q-tr>
                </template>
                </q-table>
            </div>
            
        </div>
        
       

    </q-page>
  </template>
  
<script>
import Lottie from 'vue-lottie';
import * as animationData from './creditCard2.json';
  export default {
    components: {

    Lottie
  },
  data () {
    return {
    defaultOptions: {
        animationData: animationData.default,
        loop:false,
        autoplay:true
      },

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

        { name: 'Name',align: 'center', label: 'Name', field: 'Name' },
        { name: 'Email',align: 'center', label: 'Email', field: 'Email' },
        { name: 'Gender',align: 'center', label: 'Gender', field: 'Gender' },
        { name: 'Marital_Status',align: 'center', label: 'Marital Status', field: 'Marital_Status' },
        { name: 'Address',align: 'center', label: 'Address', field: 'Address' },
        { name: 'Number',align: 'center', label: 'Phone Number', field: 'Number' },
        { name: 'DOB',align: 'center', label: 'Date Of Birth', field: 'DOB' },
        { name: 'Credit_Score',align: 'center', label: 'Credit Score', field: 'Credit_Score' },
        { name: 'Status', align: 'center',label: 'IC Upload Status', field: 'Status' },
        { name: 'Application_Status', align: 'center',label: 'Application Status', field: 'Application_Status' },
        { name: 'button', align: 'center',label: '', field: 'button' },

      ],

      data: [
        {
          name: '#A-101',
         
          Name: 'Greg G Tan',
          Email: 'greggtan99@gmail.com',
          Gender:'Male',
          Marital_Status:'Married',
          Address:"295 Comfort Court Blk 22 #10-288",
          Number:"9029 8918",
          DOB:"23/08/1999",
          Credit_Score:"700",
          Status: 'IC Uploaded',
          Application_Status:'Pending'
        },
        {
          name: '#A-246',
          
          Name: 'Warren Lynch',
          Email: 'warren@code.com',
          Gender:'Male',
          Marital_Status:'Married',
          Address:"31 Sembawang Hills Drive",
          Number:"9272 1114",
          DOB:"02/12/1991",
          Credit_Score:"780",
          Status: 'IC Uploaded',
          Application_Status:'Pending'
        },
        {
          name: '#A-2201',
          
          Name: 'Marcus Roth',
          Email: 'marcus@code.com',
          Gender:'Male',
          Marital_Status:'Divorced',
          Address:"2518 Limer Street #3-11",
          Number:"8272 6822",
          DOB:"03/10/1994",
          Credit_Score:"200",
          Status: 'IC Uploaded',
          Application_Status:'Rejected'
        },
        {
          name: '#A-1561',
          
          Name: 'Joyce Khoo',
          Email: 'joyce@code.com',
          Gender:'Female',
          Marital_Status:'Single',
          Address:"819 Plainfield Avenue Blk 200 #11-20",
          Number:"8991 1110",
          DOB:"24/01/1983",
          Credit_Score:"600",
          Status: 'IC Uploaded',
          Application_Status:'Pending'
        },
        {
          name: '#A-1611',
          
          Name: 'Mary Lim',
          Email: 'mary7@gmail.com',
          Gender:'Female',
          Marital_Status:'Married',
          Address:"123 Yio Chu Kang Ave Blk 111 #03-21",
          Number:"9941 2345",
          DOB:"21/05/1978",
          Credit_Score:"800",
          Status: 'IC Uploaded',
          Application_Status:'Pending'
        },
        
        
  
      ],


      columns2: [
        {
          name: 'name',
          required: true,
          label: 'Card Number',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },

        { name: 'Name',align: 'center', label: 'Name', field: 'Name' },
        { name: 'Email',align: 'center', label: 'Email', field: 'Email' },
        { name: 'Card_Type',align: 'center', label: 'Card_Type', field: 'Card_Type' },
        { name: 'Credit_Balance',align: 'center', label: 'Credit_Balance', field: 'Credit_Balance' },
        { name: 'Date_Created', align: 'center',label: 'Date Created', field: 'Date_Created' },
        

      ],

      data2: [
        {
          name: '4090945527283771',
         
          Name: 'Thomas Woon',
          Email: 'thomas@gmail.com',
          Card_Type:'Physical',
          Credit_Balance:'(30,000)',
          Date_Created:'10/01/2022',
          
        },
        {
          name: '4090135617283791',
         
          Name: 'Jack Yong',
          Email: 'jack@gmail.com',
          Card_Type:'Virtual',
          Credit_Balance:'0',
          Date_Created:'11/02/2022',
          
        },
        {
          name: '4090945527281235',
         
          Name: 'Emily Chong',
          Email: 'emily@gmail.com',
          Card_Type:'Physical',
          Credit_Balance:'1,300',
          Date_Created:'11/05/2022',
          
        },
        {
          name: '4083911527283771',
         
          Name: 'Gemma Chan',
          Email: 'gemma@gmail.com',
          Card_Type:'Physical',
          Credit_Balance:'12,000',
          Date_Created:'10/06/2022',
          
        },
        {
          name: '319594552721118',
         
          Name: 'Oliver Tan',
          Email: 'oliver@gmail.com',
          Card_Type:'Virtual',
          Credit_Balance:'17,345',
          Date_Created:'01/08/2022',
          
        },
        
        
        
  
      ]
    }
  },
    name: 'ErrorNotFound'
  }
</script>
  