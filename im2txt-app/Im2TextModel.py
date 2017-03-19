import tensorflow as tf
import im2txt

class DummyModel(object):
  def __init__(self, ModelPath, VocabularyPath):
    print("WARNING: Start Dummy Module only!")

  def createCaptions(self, Image):
    Sentences = ["Test", "Test", "Test"]
    return Sentences

class Im2Text(DummyModel):
  def __init__(self, ModelPath, VocabularyPath):
    print("Start Camera Captioning Demo:")
    print(" * Model Path: "+ModelPath)
    print(" * Vocabulary Path: "+VocabularyPath)

    # Build the inference graph.
    print("Load model...")
    ModelGraph = tf.Graph()
    with ModelGraph.as_default():
      Model = im2txt.inference_wrapper.InferenceWrapper()
      RestoreFunc = Model.build_graph_from_config(im2txt.configuration.ModelConfig(), ModelPath)

    ModelGraph.finalize()

    # Create the vocabulary.
    print("Load vocabulary...")
    self._Vocabulary = im2txt.vocabulary.Vocabulary(VocabularyPath)

    # Create TF session
    print("Create TF session...")
    self._Session = tf.Session(graph=ModelGraph)

    print("Restore checkpoint...")
    RestoreFunc(self._Session)

    print("Create caption generator...")
    self._Generator = im2txt.caption_generator.CaptionGenerator(Model, self._Vocabulary)
    
    
  def createCaptions(self, Image):
    Captions = self._Generator.beam_search(self._Session, Image)
  
    File = tf.gfile.GFile("Image.jpg", "w")
    File.write(Image)
  
    Sentences = []
    for Caption in Captions:
      # Ignore begin and end words.
      Sentence = [self._Vocabulary.id_to_word(Word) for Word in Caption.sentence[1:-1]]
      Sentence = " ".join(Sentence)
      Sentences.append(Sentence)
    
    return Sentences

