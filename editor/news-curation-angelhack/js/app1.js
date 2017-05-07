carouselFunc = function() {
        // $('.owl-carousel').data('owl.carousel').destroy();
        // $('.owl-carousel').owlCarousel({
        //     items:1,
        //     loop:false,
        //     center:true,
        //     margin:10,
        //     nav: true,
        //     dots: true,
        //     autoHeight:false,
        // });
}

Section = function(sec_name, sec_desc){
	this.sectionHeading = ko.observable(sec_name);
	this.head_desc = ko.observable(sec_desc);
	this.elementList = ko.observableArray([]);

	this.addElement = function(){
        var url = document.getElementById("newLink").value
        
		this.elementList.push(new Element({"label": "", "linkHead": "", "linkUrl":url, "linkComment":""}))

        document.getElementById("newLink").value = "";
	}.bind(this)

	this.removeElement = function(dynamicField){
		this.elementList.remove(dynamicField)
        console.log(dynamicField)
	}.bind(this)

    // this.setHeading = function(sec_name){
    //     this.sectionHeading = sec_name
    // }
};

var Element = function(data){
	this.label =  ko.observable(data.label);
	this.linkHead = ko.observable(data.linkHead);
	this.linkUrl = ko.observable(data.linkUrl);
	this.linkComment = ko.observable(data.linkComment);
    this.doSomething = function(dynamicField){
        console.log(dynamicField)
    }

}


function fieldModel(){
    var self = this;

    self.sectionList = ko.observableArray();
    //self.sectionList.push(new Section());

    self.removeSection = function(dynamicField){
    	self.sectionList.remove(dynamicField);
    	console.log(sectionList());
        carouselFunc();
        self.sectionList.valueHasMutated();
    }

    self.addSection = function(){
    	self.sectionList.push(new Section());
    	console.log(sectionList());	
    }


    self.addNewSection = function(formElement){
        var sec_name = document.getElementById("sec_name").value
        var sec_desc = document.getElementById("sec_desc").value

        self.sectionList.push(new Section(sec_name,sec_desc));

        document.getElementById("sec_name").value = ""
        document.getElementById("sec_desc").value = ""

        console.log(sectionList()); 
    }
}

ko.bindingHandlers.owlCarouselInitiator = {
    init: function() {
        $('.owl-carousel').owlCarousel({
            items:1,
            loop:false,
            center:true,
            margin:10,
            nav: true,
            dots: true,
            autoHeight:true,
        });
    },
    update: function(){
        $('.owl-carousel').data('owl.carousel').destroy();
        $('.owl-carousel').owlCarousel({
            items:1,
            loop:false,
            center:true,
            margin:10,
            nav: true,
            dots: true,
            autoHeight:true,
        });
    }

};



renderedHandler = function(){
    iframely.load();
}

ko.applyBindings(fieldModel);

//auto adjust height of textarea
function textAreaAdjust(o) {
  o.style.height = "1px";
  o.style.height = (o.scrollHeight)+"px";
}
//convert model to JSON
//jsonData = ko.toJSON(sectionList)