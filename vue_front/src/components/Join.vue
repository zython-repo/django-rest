<template>
	<div class="top_menu">
		<img :src="cappu" v-on:click="move">
		<h3 v-on:click="move">CAPPUCCINO</h3>
	</div>
</template>

<script>
	export default {
		name: 'Top',
		data() {
			return{
				cappu: require('../assets/cappuccino.png')
			}
		},
		methods: {
			move() {
				this.$router.push({
					name: 'Thumnail'
				})
			}
		}
	}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.top_menu img {
	vertical-align: middle;
	border-style: none;
	position: relative;
	width: 50px;
	right: 130px;
	top: 40px;
	cursor: pointer;
}
.top_menu h3 {
	font-size: 35px;
	position: relative;
	color: #BE800E;
	font-family: 'Indie Flower', cursive;
	width: 30%;
	margin: auto;
	cursor: pointer;
}
</style>
