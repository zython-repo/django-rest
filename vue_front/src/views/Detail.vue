<template>
	<div class="Detail_Home">
		<Mov></Mov>
		<h1>EZ_Frist!!</h1>
		<div v-if='list' class="result_style">
			<div class="title_Box">
				<h1>{{ list.title }}</h1>
			</div>
			<div class="content_Box">
				<p>{{ list.body }}</p>
				<p>{{ list.created_at }}</p> 
			</div>
		</div>
		<div v-else>
			<h1 class='Error_Text'>404 - Error</h1>
		</div>
	</div> 
</template>

<script>
	import { apiService } from '@/common/api.service.js';
import Mov from '@/components/Move_Bar.vue'

export default {
	name: 'Detail',
	props: {
		tag: {
			type: String,
			required: true
		}
	},
	data() {
		return {
			list: {}
		}
	},
	components: {
		Mov
	},
	methods: {
		setPageTitle(title) {
			document.title = title;
		},
		getListData() {
			let endpoint = `/api/detail/${this.tag}/`;
			apiService(endpoint)
				.then(data => {
					if (data) {
						this.list = data;
						this.setPageTitle(data.tag)
					} else {
						this.list = null;
						this.setPageTitle("404 - Page Not Found")
					}
				})    
		}
	},
	created() {
		this.getListData()
	}
}
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.Detail_Home h1 {
	font-family: 'Indie Flower', cursive;
	color: #BE800E;
}

/*.title_Box {
	position: relative;
	float: right;
	width: 600px;
	height: 600px;
	right: 5%;
	padding: 10px;
}
.content_Box {
	position: relative;
	float: left;
	width: 600px;
	height: 600px;
	left: 20%;
}*/
</style>
