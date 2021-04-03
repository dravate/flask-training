new Vue({
        el: '#covid',
	delimiters: ['<%', '%>'],
        data: {
		coviddata:  {}
	},
	methods: {
		 get_coviddata() {
                       axios
			 .get('/state')
			 .then(response => { this.coviddata = JSON.parse(response.data); })
			 .catch(error => console.log(error))
			 .finally(() => {
                              }
			 ) 
		}, 
	},
	 mounted () {
                this.get_coviddata()
        },
  
});
