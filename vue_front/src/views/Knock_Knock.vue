<template>
	<div class="thumnail">
		<Home></Home>
		<div class='result'>
			<router-link
				:to='{ name: "Search", params: { title: this.title } }'
				class='keyword'>{{ title }}
			</router-link>
		</div>
		<setFile @load='title = $event'></setFile>
	</div>
</template>

<script>
// @ is an alias to /src
import setFile from '@/components/Parsing_Bar.vue'
import Home from '@/components/Sweet_Home.vue'

export default {
	name: 'Thumnail',
	data() {
		return {
			title: ''
		}
	},
	components: {
		setFile,
		Home
	}
}
</script>

<style>
.result {
	position: relative;
	top: 90px;
	width: 700px;
	height: 50px;
	margin:auto;
}
.result a {
	color: black;
	background-color: transparent;
	font-family: Indie Flower,cursive;
	font-size: -webkit-xxx-large;
}
.result a:hover {
	color: #BE800E;
	text-decoration: none;
	background-color: transparent;
	font-family: Indie Flower,cursive;
	font-size: -webkit-xxx-large;
}
.keyword {
	text-align: center;
	top: 12px;
	position: relative;
	text-decoration: none;
}
</style>

