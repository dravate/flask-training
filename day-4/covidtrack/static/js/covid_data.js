new Vue({
        el: '#covid',
	delimiters: ['<%', '%>'],
        data: {
		coviddata: [] 
	},
	methods: {
		 get_coviddata() {
                       axios
			 .get('/locations/us')
			 .then(response => { this.coviddata = response.data; })
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
