<template>
<body>
    <div class="header">
      <div title="Compare professionally accredited courses by the Australian Computer Society for domestic students."><h1 class="title">Course Information Discoverer</h1></div>
    </div>
   
    <div class="stateGroup">
      <div class="select">
        <div class="uiLabel">University State</div>
        <select class="uidropdownstate" v-model="uniState1" id="university-states">
         <option v-for="option in orderBy(universityStates, 'state')" :key="option.id" v-bind:value="option">
            {{ option }}
          </option>
        </select>
      </div>
      
      <div class="select">
        <div class="uiLabel">University State</div>
        <select class="uidropdownstate" v-model="uniState2" id="university-states">
         <option v-for="option in orderBy(universityStates, 'state')" :key="option.id" v-bind:value="option">
           {{ option }}
         </option>
       </select>
      </div>
    </div>
    
    <div class="uniGroup">
      <div class="select">
        <div class="uiLabel">University 1</div>
        <select class="uidropdownuni" id="universities" v-model="university1">
         <option v-for="option in orderBy(filteredUnis1, 'university')" :key="option.id" v-bind:value="option">
           {{ option }}
         </option>
       </select>  
      </div>
      
      <div class="select">
        <div class="uiLabel">University 2</div>
        <select class="uidropdownuni" id="universities" v-model="university2">
         <option v-for="option in orderBy(filteredUnis2, 'university')" :key="option.id" v-bind:value="option">
           {{ option }}
         </option>
       </select>  
      </div>
    </div>
    
    <div class="courseGroup">
      <div class="select">
       <div class="uiLabel">Course 1</div>
       <select class="uidropdowncourse" id="courses" v-model="course1" @change="onCourseChange1()">
         <option v-for="option in orderBy(filteredCourses1, 'title')" :key="option.id" :value="option">
           {{ option.title }}
         </option>
       </select>
        <p>Available at {{ course1.campus }} campus. </p> 
      </div>
      
     <div class="select">
       <div class="uiLabel">Course 2</div>
       <select class="uidropdowncourse" id="courses" v-model="course2" @change="onCourseChange2()">
         <option v-for="option in orderBy(filteredCourses2, 'title')" :key="option.id" :value="option">
           {{ option.title }}
         </option>
       </select>
       <p>Available at {{ course2.campus }} campus. </p>
      </div>  
    </div>

   <div class = "lineChart">
      <div title="Fees are estimates provided by the universities and are subject to change depending on minors, electives or majors seleceted, if fees are 0 that means the fees were not provided by university."><h2>Yearly Fees Comparison</h2></div>
      <GChart
       type="LineChart"
       :options="yearlyFeesOptions"
       :data="yearlyFeesData"
      />
    </div>

    <div class = "feeChart">
      <div title="Fees are estimates provided by the universities and are subject to change depending on minors, electives or majors seleceted, if fees are 0 that means the fees were not provided by university."><h2>Total Fees Comparison</h2></div>
      <GChart
      type="ColumnChart"
      :options="totalFeesOptions"
      :data="totalFeesData"
      />
    </div>

    <div class = "uniRankingChart">
      <h2>QS 2022 World University Ranking Comparison</h2>
      <GChart
      type="BarChart"
      :options="uniRankingOptions"
      :data="uniRankingData"
      />
    </div>

    <div class = "atarChart">
      <h2>Guaranteed Entry ATAR Comparison</h2>
      <GChart
      type="ColumnChart"
      :options="atarOptions"
      :data="guaranteedAtarData"
      />
    </div>

    <div class = "unitChart">
      <h2>Course Unit Count Comparison</h2>
      <GChart
      type="ColumnChart"
      :options="options"
      :data="unitsData"
      />    
    </div>
    
    <div class="descriptionGroup">
      <div id="description">
       <div class="uiLabel" v-for="option in filteredCourseUrl1" :key="option.url"><a v-bind:href="option.url"> {{ option.university}} <br> {{ option.title }}</a> <br> Description:</div>
       <p v-for="option in filteredCourseUrl1" :key="option.id" > {{ option.description }}</p>
      </div>
      
     <div id="description">
       <div class="uiLabel" v-for="option in filteredCourseUrl2" :key="option.url"><a v-bind:href="option.url"> {{ option.university}} <br> {{ option.title }}</a> <br> Description:</div>
       <p v-for="option in filteredCourseUrl2" :key="option.id"> {{ option.description }}</p>
      </div>
    </div>

    <div class="learningGroup">
      <div id="learningOutcomes">
       <div class="uiLabel" v-for="option in filteredCourseUrl1" :key="option.url"><a v-bind:href="option.url">{{ option.university}} <br> {{ option.title }}</a> <br> Learning Outcomes:</div>
       <p v-for="option in filteredCourseUrl1" :key="option.id" > {{ option.learningOutcomes }} </p>
      </div>
      
     <div id="learningOutcomes">
       <div class="uiLabel" v-for="option in filteredCourseUrl2" :key="option.url"><a v-bind:href="option.url">{{ option.university}} <br> {{ option.title }}</a> <br> Learning Outcomes:</div>
       <p v-for="option in filteredCourseUrl2" :key="option.id"> {{ option.learningOutcomes }} </p>
      </div>
    </div>

</body>
</template>
 
<script>
import { GChart } from "vue-google-charts";
import { getAPI } from '../axios-api'
import Vue2Filters from 'vue2-filters'

export default {
  title: 'Course Information Discoverer',
  name: "App",
  mixins: [Vue2Filters.mixin],
  components: {
    GChart
  },
  data() {
    return {
      /* chart arrays */
      yearlyFeesData: [
        ["Day", "Course1", "Course2"],
        [1,  0, 0],
        [2,  0, 0],
        [3,  0, 0],
        [4,  0, 0],
        [5,  0 , 0],
      ],
      totalFeesData: [
         ['Course', 'Total Fees', { role: 'style' }],
         ['Course 1', 0, '#5a83d6'],
         ['Course 2', 0, '#de421c'],
      ],
      guaranteedAtarData: [
         ['Course', 'ATAR', { role: 'style' }],
         ['Course 1', 0, '#5a83d6'],
         ['Course 2', 0, '#de421c'],
      ],
      unitsData: [
         ['Course', 'Units', { role: 'style' }],
         ['Course 1', 0, '#5a83d6'],
         ['Course 2', 0, '#de421c'],
      ],
      uniRankingData: [
        ['Course', 'QS Ranking', { role: 'style' } ],
        ['Course 1', 0, 'color: #5a83d6'],
        ['Course 2', 0, 'color: #de421c'],
      ],
      /*Array to store api data */
      APIData: [],
      /*Arrays to store filtered course objects*/
      course1: [''],
      course2: [''],
      /*declare variables to store v-models*/
      uniState1: null,
      uniState2: null,
      university1: null,
      university2: null,
      yearlyFeesOptions: {
        chart: {
          title: "Fees to be paid over years"
        },
        hAxis: {title: 'Number of Years'},
        vAxis: {title: 'Yearly Fees in $'},
        width: 800,
        height: 400
      },
      options: {
        hAxis: {title: 'Amount Of Units Required To Graduate'},
        width: 800,
        height: 400
      },
      totalFeesOptions: {
        vAxis: {title: 'Total Fees in $'},
        width: 800,
        height: 400
      },
      uniRankingOptions: {
        hAxis: {title: '2022 QS Rankings (Lower is better)'},
        width: 800,
        height: 400
      },
      atarOptions: {
        hAxis: {title: 'ATAR is the adjusted rank (ATAR plus adjustment factors)'},
        width: 800,
        height: 400
      }
    };
  },
  methods: {
    /*on course dropdown box change event */
    onCourseChange1() {    
      /*add reset all line chart data back to 0 here*/
      for (var i = 1 ; i < 5 + 1 ; i++) {
        this.$set(this.yearlyFeesData[i], 1, 0)
      }
      /*set h axis label to course 1 title */
      this.$set(this.yearlyFeesData[0], 1, this.course1.university + " - " + this.course1.title) 
      /*update yearly fees line chart, loop through rows depending on duration and set 1st element of row to course 1 yearly fees*/
      for (i = 1 ; i < this.course1.duration + 1 ; i++) {
        this.$set(this.yearlyFeesData[i], 1, parseFloat(this.course1.yearlyFees)) 
      }
      /*update course 1 total fees column and title of column */
      this.$set(this.totalFeesData[1], 0, this.course1.university + " - " + this.course1.title)
      this.$set(this.totalFeesData[1], 1, parseFloat(this.course1.fees))
      /*update course 1 guaranteed atar column */
      this.$set(this.guaranteedAtarData[1], 0, this.course1.university + " - " + this.course1.title)
      this.$set(this.guaranteedAtarData[1], 1, parseFloat(this.course1.guaranteedAtar))
      /*update course 1 units column */
      this.$set(this.unitsData[1], 0, this.course1.university + " - " + this.course1.title)
      this.$set(this.unitsData[1], 1, parseInt(this.course1.units))
      /*update course 1 university ranking bar chart */
      this.$set(this.uniRankingData[1], 0, this.course1.university)
      this.$set(this.uniRankingData[1], 1, parseInt(this.course1.uniRanking))
    },
    onCourseChange2() {
      for (var i = 1 ; i < 5 + 1; i++) {
        this.$set(this.yearlyFeesData[i], 2, 0)
      }

      this.$set(this.yearlyFeesData[0], 2, this.course2.university + " - " + this.course2.title)

      for (i = 1 ; i < this.course2.duration + 1 ; i++) {
        this.$set(this.yearlyFeesData[i], 2, parseFloat(this.course2.yearlyFees)) 
      }

      this.$set(this.totalFeesData[2], 0, this.course2.university + " - " + this.course2.title)
      this.$set(this.totalFeesData[2], 1, parseFloat(this.course2.fees))
 
      this.$set(this.guaranteedAtarData[2], 0, this.course2.university + " - " + this.course2.title)
      this.$set(this.guaranteedAtarData[2], 1, parseFloat(this.course2.guaranteedAtar))

      this.$set(this.unitsData[2], 0, this.course2.university + " - " + this.course2.title)
      this.$set(this.unitsData[2], 1, parseInt(this.course2.units))

      this.$set(this.uniRankingData[2], 0, this.course2.university)
      this.$set(this.uniRankingData[2], 1, parseInt(this.course2.uniRanking))
    }
  },
  computed: {
    universityStates () {
      /* returns array of unique states from API Data */
      return [...new Set(this.APIData.map(({ state }) => state))] 
    },
    filteredUnis1() {
      /*returns filtered list of course objects depending on state chosen */
      var filtered = this.APIData.filter(option => !option.state.indexOf(this.uniState1)) 
      /*gets filtered list of course objects and returns a set without duplicate universities */
      return [...new Set(filtered.map(({ university }) => university))] 
    },
    filteredUnis2() {
      var filtered = this.APIData.filter(option => !option.state.indexOf(this.uniState2)) 
      return [...new Set(filtered.map(({ university }) => university))]
    },
    filteredCourses1() {
      /*returns filtered list of course objects depending on uni chosen*/
      return this.APIData.filter(option => !option.university.indexOf(this.university1)) 
    },
    filteredCourses2() {
      return this.APIData.filter(option => !option.university.indexOf(this.university2)) 
    },
    filteredCourseUrl1() {
      /*returns filtered list of course objects depending on the url of course chosen(used url instead of title because url is unique), the objects contain all fields/properties(can use in charts)*/
      return this.APIData.filter(option => !option.url.indexOf(this.course1.url)) 
    },
    filteredCourseUrl2() {
      return this.APIData.filter(option => !option.url.indexOf(this.course2.url)) 
    },
  },
  created () {
      /* get request from our django restful api and log if its successful to console */
      getAPI.get('/api/courses/',) 
         .then(response => {
           console.log('Successfully retrieved data from API')
           this.APIData = response.data
         })
         /* log failure if timeout after 5000 ms */
         .catch(err => { 
           console.log(err)
         })
  }
};
</script>


<style lang="scss">
/*class selectors */
.uiLabel{
  padding: 15px;
  font-weight: bold;
}

.stateGroup{
  padding-top: 50px; /*add padding on top of state to give a bigger gap to title */
}

.courseGroup{
  margin-bottom: 100px;
}

.lineChart{
  display: inline-block;
  border-radius: 25px;
  border: 2px solid #e3ddda;
  padding: 15px;
  margin-bottom: 50px;
}

.feeChart{
  display: inline-block;
  border-radius: 25px;
  border: 2px solid #e3ddda;
  padding: 15px;
  margin-bottom: 50px;
}

.atarChart{
  display: inline-block;
  border-radius: 25px;
  border: 2px solid #e3ddda;
  padding: 15px;
  margin-bottom: 50px;
}

.unitChart{
  display: inline-block;
  border-radius: 25px;
  border: 2px solid #e3ddda;
  padding: 15px;
  margin-bottom: 50px;
}

.uniRankingChart{
  display: inline-block;
  border-radius: 25px;
  border: 2px solid #e3ddda;
  padding: 15px;
  margin-bottom: 50px;
}


.header {
  padding: 70px;
  text-align: center;
  background: #126bbf;
  color: black;
  font-size: 30px;
  margin-bottom: 50px;
}

.descriptionGroup{
  margin-bottom: 50px;
}

.learningGroup{
  margin-bottom: 50px;
}

.uidropdownstate{ //change dropdown box style
  width: 400px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 50px;
  padding: 10px 38px 10px 16px;
  background-size: 10px;
  transition: border-color .1s ease-in-out,box-shadow .1s ease-in-out;
  border: 1px solid #ddd;
  border-radius: 3px;
  text-align-last: center;
} 

.uidropdownstate:hover {
    border: 1px solid #999;
}
.uidropdownstate:focus {
    border: 1px solid #999;
    box-shadow: 0 3px 5px 0 rgba(0,0,0,.2);
    outline: none;
}

/* remove default arrow in IE */
select::-ms-expand {
    display:none;
}

.uidropdownuni{
  width: 400px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 50px;
  padding: 10px 38px 10px 16px;
  background-size: 10px;
  transition: border-color .1s ease-in-out,box-shadow .1s ease-in-out;
  border: 1px solid #ddd;
  border-radius: 3px;
  text-align-last: center;
}

.uidropdownuni:hover {
    border: 1px solid #999;
}
.uidropdownuni:focus {
    border: 1px solid #999;
    box-shadow: 0 3px 5px 0 rgba(0,0,0,.2);
    outline: none;
}

.uidropdowncourse{
  width: 600px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 50px;
  padding: 10px 38px 10px 16px;
  background-size: 10px;
  transition: border-color .1s ease-in-out,box-shadow .1s ease-in-out;
  border: 1px solid #ddd;
  border-radius: 3px;
  text-align-last: center;
}

.uidropdowncourse:hover {
    border: 1px solid #999;
}
.uidropdowncourse:focus {
    border: 1px solid #999;
    box-shadow: 0 3px 5px 0 rgba(0,0,0,.2);
    outline: none;
}

.select{
  display:inline-block;
  padding: 10px;
}

/*id selectors*/
#description{
  display: inline-block;
  border: 2px solid #e3ddda;
  padding: 15px;
}

#learningOutcomes{
  display: inline-block;
  border: 2px solid #e3ddda;
  padding: 15px;
}

body
{
  font-family: 'Helvetica', 'Arial', sans-serif;
  color: #444444;
  background-color: #FAFAFA;
}

p{
  padding: 30px;
}

h1 { 
  color: #ffffff; 
  font-family: 'Raleway',sans-serif; 
  font-size: 50px; 
  font-weight: 525;  
  text-align: center;
}

</style>
