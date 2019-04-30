from django.db import models

# Create your models here.

# a hap-dash conception of "topics"
# TODO: this really belongs 1) in model and 2) in a data base
class Topic(models.Model):
    name = models.CharField(max_length=64)

    # this allows us to ref the object itself in a template to get it's name
    def __str__(self):
        return self.name

    # this is just here so I didn't have to refactor the template
    def subtopics(self):
        return self.subtopic_set.all()

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    text = models.TextField(default = "<p>ERROR: TEXT MISSING</p>")

    # this allows us to ref the object itself in a template to get it's name
    def __str__(self):
        return self.name

    # placehold implementation, just spits out lorem ipsum
    # real implementation is commented out above
    def text_lorem_ipsum(self):
        return '''
        <!-- some lorem ipsum -->
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac aliquet lorem, ultricies auctor sapien. Morbi non dui quis est convallis volutpat. Vestibulum convallis sapien eu placerat malesuada. Nam bibendum dictum pulvinar. Vestibulum eleifend interdum malesuada. Donec pulvinar orci vitae dignissim ullamcorper. Curabitur auctor molestie eleifend. Curabitur posuere tellus nec elementum cursus. Nulla ut ligula a diam volutpat imperdiet. Vestibulum auctor elit risus, eu suscipit justo molestie in. Proin maximus elementum purus in commodo.

Sed mattis tristique viverra. Vestibulum ut libero ornare, finibus arcu a, vehicula leo. Suspendisse vel odio et nibh congue sodales. Nunc ac eros porttitor, semper lectus a, mollis quam. Sed at neque odio. Integer sodales placerat vehicula. Nullam urna tellus, volutpat id sapien vitae, eleifend sodales ante.

<i>
Nulla ornare leo eu nunc tristique accumsan. Etiam eu risus non nulla pharetra vulputate at in lacus. Fusce nec lacinia orci. Proin facilisis nibh et pharetra imperdiet. Ut condimentum nulla felis, vitae ornare odio maximus sed. Cras aliquam mi elit, quis fermentum dolor malesuada eget. Donec a nisi a purus aliquam mattis. Integer libero eros, elementum sed libero et, suscipit facilisis purus. Maecenas gravida cursus dui et volutpat. In hac habitasse platea dictumst. In hac habitasse platea dictumst. Nulla facilisi. Praesent varius sapien elementum, semper turpis sit amet, iaculis odio. Praesent vitae orci ornare, tempus erat sed, egestas eros.
</i>

Cras viverra felis id arcu volutpat lacinia. Aliquam erat volutpat. Nam ut rutrum dolor. Proin id erat turpis. Vestibulum non molestie dolor, vitae pulvinar nunc. Duis eu mi sed eros varius accumsan non at ipsum. Curabitur quis purus viverra, molestie magna a, varius arcu. Sed congue lorem eu enim porttitor, sit amet dapibus eros laoreet. Donec hendrerit orci et leo maximus, pharetra rutrum augue porttitor. Donec id mauris sed lectus tristique tristique eu eu libero.

Vestibulum egestas tempor quam vitae congue. Pellentesque a molestie ipsum. Nulla molestie neque nec viverra dictum. Mauris quis orci sapien. Pellentesque accumsan imperdiet dui a cursus. Nunc eget nisi non arcu viverra faucibus luctus ut odio. Ut id gravida arcu. Mauris dapibus, lacus vitae tincidunt tempor, neque nibh malesuada tortor, eu bibendum odio nisi vel quam. Donec commodo, arcu id accumsan cursus, magna magna rutrum ex, eget laoreet ipsum libero ac felis. Cras lectus leo, sodales nec vehicula sed, vestibulum vitae enim. Morbi neque mauris, faucibus non feugiat ut, lobortis eu erat. 
        '''

'''
topics = {
    Topic('ELD' , set()),
    Topic('Dual Language Imersion Schools' , {'Spanish', 'Croatian'}),
    Topic('The Value of Esperanto' , {'The Esperanto Thing is a Joke'}),
    Topic('English Language Standardized Tests' , {'RIP STAR Test (not really)'}),
}

topic_lookup = { t.name : t for t in topics }
'''