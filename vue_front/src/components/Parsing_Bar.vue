<template>
	<div class="search_file">
		<label>
			<img :src="cappu">
			<input type='file' @change='getKeyword'>
		</label>
	</div>
</template>

<script>
	export default {
		name: 'setFile',
		data() {
			return{
				cappu: require('../assets/cappuccino.png')
			}
		},
		methods:{
			getKeyword(logs) {
				const file = logs.target.files[0];
				const reader = new FileReader();

				reader.onload = key => this.$emit('load', key.target.result);
				reader.readAsText(file, 'UTF-8');
			},
		}
}
</script>

<style>
.search_file {
	position: relative;
	top: 120px;
	overflow: hidden;
	display: inline-block;
}
.search_file img {
	width: 100px;
	cursor: pointer;	
}
.search_file input {
	position: absolute;
	top: 0;
	left: 0;
	z-index: -1;
	opacity: 0;
}
</style>
